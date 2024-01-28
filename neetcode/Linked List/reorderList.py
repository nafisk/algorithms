    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Function to reverse the linked list
        def reverseLL(root):
            prev = None
            while root:
                next = root.next
                root.next = prev
                prev = root
                root = next
            return prev

        # Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        second = reverseLL(slow.next)
        slow.next = None  # Split the list into two halves

        # Interleave the two halves
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        # No return statement needed as we modify the list in place

