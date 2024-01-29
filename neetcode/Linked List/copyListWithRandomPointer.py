    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        node -> node
        7 (used just for reference) -> 7 (that has actual pointers)
        '''
        # Check for an empty list
        if head is None:
            return None

        # create nodes
        mapLL = {}
        tmp = head
        while tmp:
            mapLL[tmp] = Node(tmp.val)
            tmp = tmp.next        
        
        # attach pointers
        tmp = head
        while tmp:
            node = mapLL[tmp]
            node.next = mapLL.get(tmp.next, None)
            node.random = mapLL.get(tmp.random, None)
            tmp = tmp.next
            
        return mapLL[head]
