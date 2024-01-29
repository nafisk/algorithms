    def findDuplicate(self, nums: List[int]) -> int:
        '''
            RULE: Cannot modify nums / cannot sort
                  Perform in O(1) Space Complexity
                  
          - Use FLOYDS ALGO
            - Use fast and slow pointer to find the intersections
            - Use orig. slow ptr and a new ptr to increment by 1 
                - and find new intersection between them
        '''
       
        # think of this like a graph, going from index to index
        # if there are duplicates, it will create a cyclic graph
        slow, fast = 0, 0
        while True:          
            # fast and slow pointer using array
            slow =  nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:             
                break
                
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
                
        return slow2
