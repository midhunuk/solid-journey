def getValues(stack):
    a = stack.pop()
    b = stack.pop()
    return b, a


def EvaluateExpression(exp):
    l = exp.split(' ')
    stack =[]
    for c in l:
        if(c == "+"):
            a, b = getValues(stack)
            stack.append(a + b)
        elif(c == "-"):
            a, b = getValues(stack)
            stack.append(a - b)
        elif(c == "*"):
            a, b = getValues(stack)
            stack.append(a * b)
        elif(c == "/"):
            a, b = getValues(stack)
            stack.append(a / b)
        elif(c == "**"):
            a, b = getValues(stack)
            stack.append(a ** b)
        else:
            stack.append(int(c))
             
    return stack.pop()

print(float(EvaluateExpression("2 3 1 * + 9 -")))