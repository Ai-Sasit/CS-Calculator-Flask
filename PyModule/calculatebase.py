from bitstring import Bits
#!----------------------------------------------------------------------------------!#
def DecimalToBinary(num,Num):
    Four = bin(num)[2:] ; G = bin(Num)[2:] ; Bit = list() ; Bit2 = list()
    if len(Four) > len(G): Loop = len(Four)
    elif len(Four) < len(G): Loop = len(G)
    else: Loop = len(Four)
    for i in range(1,Loop+2):
        try:
            if Four[-i] == "1":
               Bit.append(Four[-i])
            else: Bit.append("0")
        except: Bit.append("0")
    for k in range(1,Loop+2):
        try:
            if G[-k] == "1":
               Bit2.append(G[-k])
            else: Bit2.append("0")
        except: Bit2.append("0")        
    return ("").join(Bit[-1::-1])+","+("").join(Bit2[-1::-1])

def TwoComplement(num):
    Bit = list() ; Str = list()
    for i in num:
        if i == "1": Bit.append("0")
        else: Bit.append("1") 
    OneC = ("").join(Bit)
    TwoC = str(bin(int(OneC,2) + int("1",2))[2:])
    for i in range(1,len(TwoC)+2):
        try:
            if TwoC[-i] == "1":
                Str.append(TwoC[-i])
            else: Str.append("0")
        except: Str.append("0")
    return ("").join(Str[-1::-1])

def TwoComplement_SUB(num):
    Bit = list() ; Str = list()
    for i in num:
        if i == "1": Bit.append("0")
        else: Bit.append("1") 
    OneC = ("").join(Bit)
    TwoC = str(bin(int(OneC,2) + int("1",2))[2:])
    for i in range(1,len(TwoC)+1):
        try:
            if TwoC[-i] == "1":
                Str.append(TwoC[-i])
            else: Str.append("0")
        except: Str.append("0")
    return ("").join(Str[-1::-1])

def subBitbinary(T,S,loop):
    N4S = str(bin(int(T,2) + int(S,2))[2:]) ; S4 = list()
    for i in range(1,loop+1):
        try:
            if N4S[-i] == "1":
                S4.append(N4S[-i])
            else: S4.append("0")
        except: S4.append("0")
    return ("").join(S4[-1::-1])

def addBitbinary(T,S,loop):
    N4A = str(bin(int(T,2) - int(S,2))[2:]) ; A4 = list()
    for i in range(1,loop+1):
        try:
            if N4A[-i] == "1":
                A4.append(N4A[-i])
            else: A4.append("0")
        except: A4.append("0")
    return ("").join(A4[-1::-1])
#!----------------------------------------------------------------------------------!#
def BoothAlgorithm(m,q):
    M,Q = DecimalToBinary(abs(m),abs(q)).split(",") ; Booth = list()
    Qsub1 = "0" ; Count = len(Q) ; A ="0"*len(Q) ; Cir = 0
    B = TwoComplement(M)
    if m < 0: 
        M = TwoComplement_SUB(M)
        B = TwoComplement(M)
    if q < 0: Q = TwoComplement_SUB(Q)
    Booth.append([A,Q,Qsub1,M,"Initial","-"])
    while Count != 0 and m < 0:
        if (Q[-1] == "0" and Qsub1 == "0") or (Q[-1] == "1" and Qsub1 == "1"):
            Qsub1 = Q[-1] ; Cir += 1
            Q = A[-1] + Q[:-1]
            if A[0] == "1":
                A = "1" + A[:-1]
            else: A = "0"+ A[:-1]
            Booth.append([A,Q,Qsub1,M,"R-Shift",Cir])
        elif (Q[-1] == "0" and Qsub1 == "1"):
            A = subBitbinary(A,TwoComplement_SUB(B),len(A)) ; Cir += 1
            Booth.append([A,Q,Qsub1,M,"A = A + B",Cir])
            Qsub1 = Q[-1]
            Q = A[-1] + Q[:-1]
            A = "1"+ A[:-1]
            Booth.append([A,Q,Qsub1,M,"R-Shift"," "])
        elif (Q[-1] == "1" and Qsub1 == "0"):
            A = subBitbinary(A,B,len(A)) ; Cir += 1
            Booth.append([A,Q,Qsub1,M,"A = A - B",Cir])
            Qsub1 = Q[-1]
            Q = A[-1] + Q[:-1]
            A = "0" + A[:-1]
            Booth.append([A,Q,Qsub1,M,"R-Shift"," "])
        Count -= 1
    while Count != 0:
        if (Q[-1] == "0" and Qsub1 == "0") or (Q[-1] == "1" and Qsub1 == "1"):
            Qsub1 = Q[-1] ; Cir += 1
            Q = A[-1] + Q[:-1]
            if A[0] == "1":
                A = "1" + A[:-1]
            else: A = "0"+ A[:-1]
            Booth.append([A,Q,Qsub1,M,"R-Shift",Cir])
        elif (Q[-1] == "0" and Qsub1 == "1"):
            A = addBitbinary(A,B,len(A)) ; Cir += 1
            Booth.append([A,Q,Qsub1,M,"A = A + B",Cir])
            Qsub1 = Q[-1]
            Q = A[-1] + Q[:-1]
            A = "0"+ A[:-1]
            Booth.append([A,Q,Qsub1,M,"R-Shift"," "])
        elif (Q[-1] == "1" and Qsub1 == "0"):
            A = subBitbinary(A,B,len(A)) ; Cir += 1
            Booth.append([A,Q,Qsub1,M,"A = A - B",Cir])
            Qsub1 = Q[-1]
            Q = A[-1] + Q[:-1]
            A = "1" + A[:-1]
            Booth.append([A,Q,Qsub1,M,"R-Shift"," "])
        Count -= 1
    return Booth
#!----------------------------------------------------------------------------------!#
def DecToBin(num):
    Four = bin(num)[2:] ; Bit = list()
    for i in range(1,len(Four)+2):
        try:
            if Four[-i] == "1":
               Bit.append(Four[-i])
            else: Bit.append("0")
        except: Bit.append("0")
    return ("").join(Bit[-1::-1])

def addsubBinary(B1,B2,Operand):
    if Operand == "+":
        return bin(int(B1,2) + int(B2,2))[2:]
    elif Operand == "-":
        return bin(int(B1,2) - int(B2,2))[2:]
    else: 
        return "Error: Invalid Operand!"

def TwoToBin(Dec):
    binary = DecToBin(Dec)
    Two = TwoComplement_SUB(binary)
    return Two

def BinToDec(binary):
    a = Bits(bin=binary)
    return a.int

def octalToDecimal(n):  
    num = n; 
    dec_value = 0; 
    base = 1; 
    temp = num; 
    while (temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
        dec_value += last_digit * base; 
        base = base * 8; 
    return dec_value; 
