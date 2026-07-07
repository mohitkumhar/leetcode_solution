class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1 for _ in range(n)]
        max_lis = 1

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if (LIS[j] + 1) > LIS[i]:
                        LIS[i] = LIS[j] + 1
                        max_lis = max(max_lis, LIS[i])

        return max_lis
