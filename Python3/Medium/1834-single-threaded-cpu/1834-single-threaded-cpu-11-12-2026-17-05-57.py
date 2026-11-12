class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        n = len(tasks)
        orderedTasks = []

        for i in range(n):
            orderedTasks.append((tasks[i][0], tasks[i][1], i))

        orderedTasks.sort()

        ans = []
        currTime = 0
        heap = []
        i = 0

        while len(ans) < n:

            while i < n and orderedTasks[i][0] <= currTime:
                enqueTime, processingTime, idx = orderedTasks[i]
                heapq.heappush(heap, (processingTime, idx))
                i += 1

            if not heap:
                currTime = orderedTasks[i][0]
                continue

            processingTime, idx = heapq.heappop(heap)

            currTime += processingTime
            ans.append(idx)

        return ans
