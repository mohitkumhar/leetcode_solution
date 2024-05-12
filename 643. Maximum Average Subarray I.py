class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        sum = 0
        for i in range(k):
            sum += nums[i]
        
        window_start= 0
        window_end = k

        max_sum = sum
        
        while(window_end < len(nums)):

            sum -= nums[window_start]
            window_start += 1

            sum += nums[window_end]
            window_end += 1

            max_sum = max(sum, max_sum)
        
        return max_sum / float(k)




