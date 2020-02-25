from flask import Flask, render_template as render, request
from PyModule.calculatebase import *
from PyModule.datastructure import *
app = Flask(__name__, static_url_path='/static')
@app.route('/')
def Index():
    return render('index.html')

@app.route('/Booth')
def Booth():
    return render('Booth.html')


@app.route('/Boothresult',methods = ['POST', 'GET'])
def Boothresult():
    if request.method == 'POST':
        try:
            result = request.form.to_dict()
            Qx = int(result["Qx"])
            Mx = int(result["Mx"])
            Booths = BoothAlgorithm(Qx,Mx)
        except:
            Booths = [["Invalid","Invalid","Invalid","Invalid","Invalid","Invalid"]]
        finally:
            try:
                Ans=["Binary: "+str((Booths[-1])[0]+(Booths[-1])[1]) , "Decimal: "+str(int(Qx)*int(Mx))]
            except:
                Ans=["Please enter an answer."]
        return render('Booth.html',Booths = Booths,Ans = Ans)


@app.route('/Base')
def Base():
    return render('Base.html')

@app.route('/Baseresult',methods = ['POST', 'GET'])
def Baseresult():
    if request.method == 'POST':
        try:
            result = request.form.to_dict()
            Base = result["Base"]
            O = int(result["option"])
            if O == 1:
                Base = str(Base)
                B = str(BinToDec(Base)) 
                B2 = oct(int(B))[2:]
                B3 = hex(int(B))[2:].upper()
            elif O == 2:
                Base = int(Base)
                B = DecToBin(Base)
                B2 = oct(Base)[2:]
                B3 = hex(Base)[2:].upper()
            elif O == 3:
                Base = int(Base)
                B = str(octalToDecimal(Base))
                B2 = DecToBin(int(B))
                B3 = hex(int(B))[2:].upper()
            elif O == 4:
                B = str(int(Base,16))
                B2 = oct(int(B))[2:]
                B3 = DecToBin(int(B))
        except:
            B = "Invalid"
            B2 = "Invalid"
            B3 = "Invalid"
        finally:
            if O == 1:
                B += " , Decimal" 
                B2 += " , Octal"
                B3 += " , Hexadecimal" 
                
            elif O == 2:
                B += " , Binary"
                B2 += " , Octal"
                B3 += " , Hexadecimal"
            elif O == 3:
                B += " , Decimal"
                B2 += " , Binary"
                B3 += " , Hexadecimal"
            elif O == 4:
                B += " , Decimal"
                B2 += " , Octal"
                B3 += " , Binary"
        return render('Base.html',B = B,B2 = B2,B3 = B3)

@app.route('/Fix')
def Fix():
    return render('Fix.html')

@app.route('/Fixresult',methods = ['POST', 'GET'])
def Fixresult():
    if request.method == 'POST':
        try:
            result = request.form.to_dict()
            F = str(result["Fix"])
            O = int(result["option"])
            if O == 1:To = PreToIn(F) + " , Prefix to Infix"
            elif O == 2:To = PostToIn(F)+ " , Postfix to Infix"
            elif O == 3:To = InToPre(F)+ " , Infix to Prefix"
            elif O == 4:To = InToPost(F)+ " , Infix to Postfix"
            elif O == 5:To = PreToPost(F)+ " , Prefix to Postfix"
            elif O == 6:To = PostToPre(F)+ " , Postfix to Prefix"
        except:
            To = "Invalid"
        return render('Fix.html',To = To)


@app.route('/Two')
def Two():
    return render('Two.html')

@app.route('/Tworesult',methods = ['POST', 'GET'])
def Tworesult():
    if request.method == 'POST':
        try:
            result = request.form.to_dict()
            Number = int(result["Two"])
            Dec = DecToBin(Number)
            Bin = TwoComplement_SUB(Dec)
        except:
            Dec = "invalid number"
            Bin = "invalid number"
        finally:
            try:
                Dec += f" , ({Number})"
                Bin += f" , (-{Number})"
            except:
                pass
        return render('Two.html',Dec = Dec, Bin = Bin)

@app.route('/Contact')
def Contact():
    return render('Contact.html')

if __name__ == '__main__':
    app.run(debug = True)