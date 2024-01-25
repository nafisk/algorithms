    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                
                # set temp dif at index
                res[stackIndex] = (i - stackIndex) 
                
            stack.append([t, i])
            
        return res
