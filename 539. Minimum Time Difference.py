class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for i in timePoints:
            h, m = map(int, i.split(':'))
            minutes.append(h * 60 + m)
        minutes.sort()
        min_diff = float('inf')

        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        # handling midnight case
        diff = 1440 + minutes[0] - minutes[-1]
        min_diff = min(min_diff, diff)

        return min_diff
