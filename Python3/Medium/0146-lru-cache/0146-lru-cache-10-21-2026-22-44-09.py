class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]

            val = self.map.pop(key)
            self.map[key] = val

            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            val = self.map.pop(key)
            self.map[key] = value

            return val

        if len(self.map) == self.n:
            self.map.pop(next(iter(self.map)))
            self.map[key] = value
        else:
            self.map[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
