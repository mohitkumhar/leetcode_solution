class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        left_sum = 1
        for i in range(n):
            ans[i] = left_sum
            left_sum *= nums[i]git

        right_sum = 1
        for j in range(n-1, -1, -1):
            ans[j] *= right_sum
            right_sum *= nums[j]

        return ans
