class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def _add_to_tail(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._add_to_tail(node)

            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove_node(self.cache[key])
        
        elif len(self.cache) >= self.capacity:
            lru = self.head.next
            self._remove_node(lru)
            del self.cache[lru.key]
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_tail(new_node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)