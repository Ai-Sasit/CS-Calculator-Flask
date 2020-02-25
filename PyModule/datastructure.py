def PostToIn(postfix, Stack = list()):
    def isOperand(x): 
        return ((x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'))    
    for i in postfix:      
        if isOperand(i): Stack.insert(0, i)  
        else: 
            op1 = Stack[0]  
            Stack.pop(0)  
            op2 = Stack[0]  
            Stack.pop(0)  
            Stack.insert(0, "(" + op2 + i + op1 + ")")  
    return (Stack[0])[1:-1]

def PreToIn(Prefix,Stack = list()):
    def isOperand(x):
        if x == "+" :  return True
        elif x == "-" :  return True       
        elif x == "/" :  return True
        elif x == "*" :  return True    
        else: return False;
    length = len(Prefix)
    for i in range(length-1,-1,-1):
        if isOperand(Prefix[i]):
            op1 = Stack[-1]; Stack.pop()
            op2 = Stack[-1]; Stack.pop()
            temp = "(" + op1 + Prefix[i] + op2 + ")"
            Stack.append(temp)
        else: Stack.append(Prefix[i])
    return (Stack[-1])[1:-1]

def PostToPre(postfix,Stack = list()):
    def isOperator2(x):  
        if x == "+" :  return True
        elif x == "-" :  return True       
        elif x == "/" :  return True
        elif x == "*" :  return True    
        else: return False
    length = len(postfix)   
    for i in range(length): 
        if isOperator2(postfix[i]): 
            op1 = Stack[-1];  Stack.pop()
            op2 = Stack[-1];  Stack.pop()
            temp = postfix[i] + op2 + op1
            Stack.append(temp)
        else : Stack.append(postfix[i])
    return Stack[-1]

def PreToPost(Prefix,Stack = list()):
    operators = set(['+','-','*','/'])
    for ind, letter in reversed(list(enumerate(Prefix))):
        if letter not in operators:
            Stack.append(letter)
        else:
            firstExp = Stack.pop()
            secondExp = Stack.pop()
            result = firstExp + secondExp + letter
            Stack.append(result)
    return Stack.pop()
 
def InToPre(Infix, Stack = list()):
    def reverse(str):
        return("".join(reversed(str)))
    def priority(operator):
        if operator == '+' or operator == '-': return 1
        elif operator == '*' or operator == '/' or operator == '%': return 2
        elif operator == '^': return 3
        else: return 0

    Infix = reverse(Infix)
    prefixString = str()
    for i in range(0, len(Infix)):
        if Infix[i].isalpha():
            prefixString += Infix[i]
        elif Infix[i] == ')' or Infix[i] == ']' or Infix[i] == '}':
            Stack.append(Infix[i])
        elif Infix[i] == '(' or Infix[i] == '[' or Infix[i] == '{':
            if Infix[i] == '(':
                while Stack[-1] != ')':
                    prefixString += Stack.pop()
                Stack.pop()
            if Infix[i] == '[':
                while Stack[-1] != ']':
                    prefixString += Stack.pop()
                Stack.pop()
            if Infix[i] == '{':
                while Stack[-1] != '}':
                    prefixString += Stack.pop()
                Stack.pop()
        else:
            if len(Stack) == 0:
                Stack.append(Infix[i])
            else:
                if priority(Infix[i]) >= priority(Stack[-1]):
                    Stack.extend(Infix[i])
                elif priority(Infix[i]) < priority(Stack[-1]):
                    prefixString += Stack.pop()
                    position = len(Stack) - 1
                    while position >= 0 and priority(Stack[position]) > priority(Infix[i]):
                        prefixString += Stack.pop()
                        position -= 1
                        if position < 0:
                            break
                    Stack.extend(Infix[i])
    while len(Stack) != 0:
        prefixString += Stack.pop()
    prefixString = reverse(prefixString)
    return prefixString
 
def InToPost(Infix,Stack = list()):
    def priority(operator):
        if operator == '+' or operator == '-': return 1
        elif operator == '*' or operator == '/' or operator == '%': return 2
        elif operator == '^': return 3
        else: return 0

    postfixString = str()
    for i in range(0, len(Infix)):
        if Infix[i].isalpha():
            postfixString += Infix[i]
        elif Infix[i] == '(' or Infix[i] == '[' or Infix[i] == '{':
            Stack.append(Infix[i])
        elif Infix[i] == ')' or Infix[i] == ']' or Infix[i] == '}':
            if Infix[i] == ')':
                while Stack[-1] != '(':
                    postfixString += Stack.pop()
                Stack.pop()
            if Infix[i] == ']':
                while Stack[-1] != '[':
                    postfixString += Stack.pop()
                Stack.pop()
            if Infix[i] == '}':
                while Stack[-1] != '{':
                    postfixString += Stack.pop()
                Stack.pop()
        else:
            if len(Stack) == 0:
                Stack.append(Infix[i])
            else:
                if priority(Infix[i]) > priority(Stack[-1]):
                    Stack.extend(Infix[i])
                elif priority(Infix[i]) <= priority(Stack[-1]):
                    postfixString += Stack.pop()
                    position = len(Stack) - 1
                    while position >= 0 and priority(Stack[position]) == priority(Infix[i]):
                        postfixString += Stack.pop()
                        position -= 1
                        if position < 0:
                            break
                    Stack.extend(Infix[i])
    while len(Stack) != 0:
        postfixString += Stack.pop()
    return postfixString
