class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        next_prev = nums[0]
        prev = max(nums[0], nums[1])
        ans = 0

        for i in range(2, n):
            take = nums[i] + next_prev
            skip = prev

            ans = max(take, skip)

            next_prev = prev
            prev = ans

        return ans
