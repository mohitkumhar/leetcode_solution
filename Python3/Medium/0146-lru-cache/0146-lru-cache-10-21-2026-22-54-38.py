
class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.cache = []

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            value = self.cache[i]
            if value[0] == key:
                self.cache.pop(i)
                self.cache.append((key, value[1]))

                return value[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            node = self.cache[i]

            if node[0] == key:
                self.cache.pop(i)
                self.cache.append((key, value))

                return

        if self.n == len(self.cache):
            self.cache.pop(0)
            self.cache.append((key, value))
        else:
            self.cache.append((key, value))



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)