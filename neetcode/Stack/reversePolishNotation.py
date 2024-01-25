def evalRPN(self, tokens: List[str]) -> int:
    '''
        iterate thru list
        when num, add to stack
        when op, pop stack twice, operate, add back to stack
        return top of stack
    '''
    if len(tokens) < 3:
        return int(tokens[0])
    
    numStack = []
    
    for t in tokens:
        
        if t == "+":
            x2, x1 = numStack.pop(), numStack.pop()
            numStack.append(x1 + x2)
        elif t == "-":
            x2, x1 = numStack.pop(), numStack.pop()
            numStack.append(x1 - x2)
        elif t == "*":
            x2, x1 = numStack.pop(), numStack.pop()
            numStack.append(x1 * x2)
        elif t == "/":
            x2, x1 = numStack.pop(), numStack.pop()
            numStack.append(int(x1 / x2))
        else:
            numStack.append(int(t))
            
    return numStack[-1]