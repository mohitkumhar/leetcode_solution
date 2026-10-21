

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.head = None
        self.tail = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.n = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val

            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            return

        if len(self.cache) == self.n:
            self.cache.pop(next(iter(self.cache)))
            self.cache[key] = value
        else:
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)