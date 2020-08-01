import arithmetic as ar
from tkinter import * 

ops = ["+", "-", "*", "/", "%", "^"]


def postf(exp):
    varStack = []
    opStack = []

    postfix = "["
    infix = exp 

    def precedence(ch):
        level1 = ["+", "-"]
        level2 = ["/", "*"]
        level3 = ["^"]

        if ch in level1:
            return 1
        elif ch in level2:
            return 2
        elif ch in level3:
            return 3
        else:
            return 0


    for i in range(len(infix)):
        item = infix[i]
        if item == " ":
            pass
        elif item == "(":
            opStack.append("(")
        elif item not in ops:
            postfix += item
        elif item in ops:
            postfix += "]"
            while  len(opStack) > 0 and precedence(item) <= precedence(opStack[-1]):
                postfix += opStack.pop()
            opStack.append(item)
            postfix += "["

    postfix += "]"
    while(len(opStack) > 0):
        postfix += opStack.pop()
    return postfix

        
def eval(a, b, exp):
    if exp == "+":
        r = ar.addition(a, b)
    if exp == "-":
        r = ar.subtract(a, b)
    if exp == "*":
        r = ar.multiplication(a, b)
    if exp == "/":
        r = ar.division(a, b)
    if exp == "%":
        r = ar.reminder(a, b)
    if exp == "#":
        r = ar.division_int(a, b)
    if exp == "^":
        r = ar.exponent(a, b)
    
    return r 

def evaluate_postfix(pf):
    varStack = []
    result = ""
    for i in range(len(pf)):
        item = pf[i]
        if item in ops:
            a = varStack.pop()
            b = varStack.pop()
            r = eval(a, b, item)
            varStack.append(r)
        elif item == "[":
            buffer = ""
            j = i+1
            while pf[j] != "]":
                buffer += pf[j]
                j = j + 1
            i = len(buffer) + 2
            val = float(buffer)
            varStack.append(val)
    
    return varStack[0]


    



def Calculate(infix):
    postfix = postf(infix)
    print(postfix)
    result = evaluate_postfix(postfix)
    return result

