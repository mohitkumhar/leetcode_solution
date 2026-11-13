class Solution:
    def leastInterval(self, tasks: list[str], gap: int) -> int:
        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        heap = []

        for key, values in freq.items():
            heapq.heappush(heap, -values)

        time = 0

        while heap:
            temp = []

            for i in range(gap + 1):
                if heap:
                    temp.append(-heapq.heappop(heap) - 1)

            for freq in temp:
                if freq > 0:
                    heapq.heappush(heap, -freq)

            if heap:
                time += gap + 1
            else:
                time += len(temp)

        return time
