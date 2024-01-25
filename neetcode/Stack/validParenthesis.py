    def isValid(self, s: str) -> bool:
        
        # Return False if string length is odd
        if len(s) % 2 != 0:
            return False
        
        # Map closing brackets to their corresponding opening brackets
        hmap = {')': '(', '}':'{', ']': '['}
        stack = []

        i = 0
        while i < len(s):
            
            # Check for closing bracket
            if s[i] in hmap:
                # Stack not empty, compare top with mapped opening bracket
                if stack:
                    if stack[-1] == hmap[s[i]]:
                        stack.pop()
                    else:
                        return False
                # Stack empty, but found closing bracket
                else:
                    return False
            
            # Add opening bracket to stack
            else:
                stack.append(s[i])
            
            i += 1
            
        # Return True if stack is empty, else False
        return False if stack else True

