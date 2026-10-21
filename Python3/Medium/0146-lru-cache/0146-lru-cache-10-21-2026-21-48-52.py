# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#         self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.queue = []

    def get(self, key: int) -> int:
        for i in range(len(self.queue)):
            value = self.queue[i]
            if value[0] == key:
                val = value[1]
                self.queue.pop(i)
                self.queue.append((key, val))

                return val
        return -1

    def put(self, key: int, v: int) -> None:

        for i in range(len(self.queue)):
            value = self.queue[i]

            if value[0] == key:
                val = value[1]
                self.queue.pop(i)
                self.queue.append((key, v))

                return

        if len(self.queue) == self.n:
            self.queue.pop(0)
            self.queue.append((key, v))
        else:
            self.queue.append((key, v))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
