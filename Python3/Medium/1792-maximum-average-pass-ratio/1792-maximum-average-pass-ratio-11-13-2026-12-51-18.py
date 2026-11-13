class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        n = len(classes)

        heap = []

        for i in range(n):
            currRatio = classes[i][0] / classes[i][1]
            newRatio = (classes[i][0] + 1) / (classes[i][1] + 1)

            delta = newRatio - currRatio

            heapq.heappush(heap, (-delta, i))

        while extraStudents > 0:

            delta, idx = heapq.heappop(heap)

            classes[idx][0] += 1
            classes[idx][1] += 1

            currRatio = classes[idx][0] / classes[idx][1]
            newRatio = (classes[idx][0] + 1) / (classes[idx][1] + 1)

            newDelta = newRatio - currRatio

            heapq.heappush(heap, (-newDelta, idx))

            extraStudents -= 1

        ratio = 0

        for i in range(n):
            ratio += classes[i][0] / classes[i][1]

        return ratio / n
