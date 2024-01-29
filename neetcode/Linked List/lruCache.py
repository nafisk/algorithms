class DLL():
    
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
     
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # head: least recently used, tail: most recently used 
        # head <-> __ <-> __ <-> tail
        self.head = DLL(0, 0) # right
        self.tail = DLL(0, 0) # left

        # make linear linked list, not curculalr
        self.head.next, self.tail.prev = self.tail, self.head
        
    def remove(self, node): # removes node at position
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
       
    def insert(self, node): # inserts at head
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # update DLL for LRU
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = DLL(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
            

