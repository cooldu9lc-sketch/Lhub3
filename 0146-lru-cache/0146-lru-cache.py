class Node:
    def __init__(self, val=0, key=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def remove(self):
        self.prev.next, self.next.prev = self.next, self.prev

    def insert(self, tail):
        self.prev = tail.prev
        self.next = tail
        self.prev.next = self.next.prev = self

class LRUCache:
    def __init__(self, capacity: int):
        self.d = {}
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
            
        node = self.d[key]
        # Move the existing node to the tail (most recently used)
        node.remove()
        node.insert(self.tail)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            # Update value and move to tail
            node.val = value
            node.remove()
            node.insert(self.tail)
        else:
            # FIX: Ensure both value and key are passed to the Node
            new_node = Node(val=value, key=key)
            self.d[key] = new_node
            new_node.insert(self.tail)
            self.size += 1
            
            # Eviction logic
            if self.size > self.cap:
                lru_node = self.head.next
                lru_node.remove()
                del self.d[lru_node.key] # Safe because we know the key is accurate now
                self.size -= 1