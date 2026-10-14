class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        n = len(obstacles)
        result = [1] * n
        LIS = []

        for i in range(n):
            idx = bisect.bisect_right(LIS, obstacles[i])

            if idx == len(LIS):
                LIS.append(obstacles[i])
            else:
                LIS[idx] = obstacles[i]

            result[i] = idx + 1

        return result
