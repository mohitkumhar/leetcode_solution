class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        n = len(tasks)
        orderedTasks = []

        for i in range(n):
            orderedTasks.append((tasks[i][0], tasks[i][1], i))

        orderedTasks.sort(key=lambda x: x[0])

        heap = []
        ans = []

        i = 0
        time = orderedTasks[0][0]

        while len(ans) < n:

            while i < n and orderedTasks[i][0] <= time:
                heapq.heappush(heap, (orderedTasks[i][1], orderedTasks[i][2]))
                i += 1

            if not heap:
                time = orderedTasks[i][0]
                continue

            processTime, idx = heapq.heappop(heap)

            ans.append(idx)
            time += processTime

        return ans
