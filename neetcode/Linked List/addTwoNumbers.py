    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        l1 = [2,6,3,1], l2 = [5,6,4]
        l3 = [7]
        
        '''
        
        
        resLL = ListNode()
        carry = 0
        tmp = resLL
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            res = val1 + val2 + carry
            
            rem = res % 10
            carry = res // 10
            
            tmp.next = ListNode(rem, None)
            tmp = tmp.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        if carry:
            tmp.next = ListNode(carry)
            
        return resLL.next
