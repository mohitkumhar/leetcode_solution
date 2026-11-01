class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for x, y in points:
            dist = x * x + y * y

            heapq.heappush(heap, (-dist, x, y))

            while len(heap) > k:
                heapq.heappop(heap)

        result = []

        for dist, x, y in heap:
            result.append([x, y])
        return result
