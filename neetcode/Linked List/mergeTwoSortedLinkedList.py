    def mergeTwoLists(self, lst1: Optional[ListNode], lst2: Optional[ListNode]) -> Optional[ListNode]:
        '''            
            if list1 >= list2: tmp.next = list1, tmp = tmp.next 
            else: tmp.next = list2, tmp = tmp.next 
            
            if list1= tmp.append(list[:-1])
            if list2= tmp.append(list[:-1])
            
        '''
        
        head = ListNode(None)
        tmp = head
        
        while lst1 and lst2:
            if lst1.val <= lst2.val:
                tmp.next = lst1
                lst1 = lst1.next
            else:
                tmp.next = lst2
                lst2 = lst2.next
            tmp = tmp.next

        
        if lst1:
            tmp.next = lst1
        else:
            tmp.next = lst2
        
        return head.next

