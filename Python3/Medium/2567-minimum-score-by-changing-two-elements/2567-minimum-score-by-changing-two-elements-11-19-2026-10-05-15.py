class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        ans = min(nums[n - 1] - nums[2], nums[n - 2] - nums[1], nums[n - 3] - nums[0])

        return ans
