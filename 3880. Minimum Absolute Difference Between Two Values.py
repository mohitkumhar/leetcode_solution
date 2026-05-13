class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = float('inf')
        n = len(nums)

        for i in range(n):
            for j in range(n):
                if nums[i] == 1 and nums[j] == 2:
                    result = min(result, abs(i - j))
        return result if result != float('inf') else -1
