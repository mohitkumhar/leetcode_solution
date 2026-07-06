class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key= lambda x: (x[0], -x[1]))

        max_end = 0
        ans = 0

        for interval in intervals:
            end = interval[1]
            if max_end < end:
                ans += 1
                max_end = end

        return ans
