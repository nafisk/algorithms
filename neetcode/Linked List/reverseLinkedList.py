    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        tmp = None
        while head:
            nxt = head.next
            head.next = tmp
            tmp = head
            head = nxt
        return tmp
