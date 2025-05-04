class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev_end = float('-inf')
        count = 0
        
        for start, end in intervals:
            if start < prev_end:
                count += 1
            
            else:
                prev_end = end
        
        return count

        