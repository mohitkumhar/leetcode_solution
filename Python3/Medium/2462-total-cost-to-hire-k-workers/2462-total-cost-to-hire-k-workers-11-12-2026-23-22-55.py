class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:

        heap1 = []
        heap2 = []

        hired = 0

        count = 0

        i = 0
        j = len(costs) - 1

        while hired < k:

            while len(heap1) < candidates and i <= j:
                heapq.heappush(heap1, costs[i])
                i += 1

            while len(heap2) < candidates and j >= i:
                heapq.heappush(heap2, costs[j])
                j -= 1

            a = heap1[0] if heap1 else float('inf')
            b = heap2[0] if heap2 else float('inf')

            if a <= b:
                count += heapq.heappop(heap1)
            else:
                count += heapq.heappop(heap2)

            hired += 1

        return count
