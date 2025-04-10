class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        end = intervals[0][1]
        start = intervals[0][0]
        ans = []

        for interval in intervals:
            if end >= interval[0]:
                if ans:
                    ans.pop()

                merged = [min(start, interval[0]), max(interval[1], end)]
                ans.append(merged)
                start = merged[0]
                end = merged[1]

            else:
                ans.append(interval)
                start = interval[0]
                end = interval[1]
        
        return ans
