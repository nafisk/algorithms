
def parents(n):
    
    res = []
    stack = []
    
    def backtrack(openN, closeN):
        
        # end if same number of open and close parens
        if openN == closeN == n:
            res.append("".join(stack))
            return
        
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closeN)
            stack.pop()
        
        if closeN < openN:
            stack.append(")")
            backtrack(openN, closeN + 1)
            stack.pop()
        
    
    
    backtrack(0, 0)
    return res
    
    
# take argument from command line and insert into function
if __name__ == "__main__":
    import sys
    print(parents(int(sys.argv[1])))