class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [abs(num) for num in nums]

        nums.sort()
        n = len(nums)

        ans = 0

        for i in range(n // 2):
            ans -= nums[i] * nums[i]

        for j in range(n // 2, n):
            ans += nums[j] * nums[j]

        return ans
