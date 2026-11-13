class Solution:
    def leastInterval(self, tasks: list[str], gaps: int) -> int:

        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, -value)

        time = 0

        while heap:
            temp = []
            for _ in range(gaps + 1):
                if heap:
                    temp.append(-heapq.heappop(heap) - 1)

            for freq in temp:
                if freq > 0:
                    heapq.heappush(heap, -freq)

            if not heap:
                time += len(temp)

            else:
                time += gaps + 1

        return time
