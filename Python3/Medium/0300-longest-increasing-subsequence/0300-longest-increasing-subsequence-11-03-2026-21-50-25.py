class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:        
        n = len(nums)

        LIS = [1] * n

        max_lis = 1

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
                    max_lis = max(max_lis, LIS[i])
        
        return max_lis

