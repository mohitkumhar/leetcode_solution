class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        def checkSmallestStart(target):
            left = 0
            right = len(starts) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if starts[mid][0] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            if left < len(intervals):
                return starts[left][1]
            return -1

        starts = []

        for i in range(len(intervals)):
            starts.append((intervals[i][0], i))

        starts.sort()

        answer = [-1] * len(intervals)

        for i in range(len(intervals)):
            target = intervals[i][1]

            answer[i] = checkSmallestStart(target)

        return answer
