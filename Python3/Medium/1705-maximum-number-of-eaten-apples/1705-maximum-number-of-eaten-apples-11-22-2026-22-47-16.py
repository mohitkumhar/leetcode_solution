class Solution:
    def eatenApples(self, apples: list[int], days: list[int]) -> int:
        heap = []  # (day, apple)
        n = len(apples)
        currDay = 0
        count = 0

        while currDay < n or heap:
            if currDay < n and apples[currDay] > 0:
                heapq.heappush(heap, (currDay + days[currDay], apples[currDay]))

            while heap and heap[0][0] <= currDay:
                heapq.heappop(heap)

            if heap:
                day, apple = heapq.heappop(heap)

                count += 1
                if apple > 1:
                    heapq.heappush(heap, (day, apple - 1))

            currDay += 1

        return count
