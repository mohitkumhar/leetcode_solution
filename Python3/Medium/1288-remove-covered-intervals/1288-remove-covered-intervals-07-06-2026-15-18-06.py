class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def check(x, y):
            a, b = x[0], x[1]
            c, d = y[0], y[1]

            if (c <= a and b <= d):
                return 1
            if (a <= c and d <= b):
                return 2

        n = len(intervals)
        covered = [False] * n

        for i in range(n):
            for j in range(i + 1, n):
                check_cover = check(intervals[i], intervals[j])
                
                if check_cover == 1:
                    covered[i] = True
                elif check_cover == 2:
                    covered[j] = True

        return covered.count(False)
