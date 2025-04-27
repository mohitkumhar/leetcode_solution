class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining = 0
        prev_end = 0

        for start, end in intervals:
            if prev_end < end:
                remaining += 1
                prev_end = end
    
        return remaining
            
            

