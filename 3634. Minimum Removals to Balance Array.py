class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        j = 0
        ans = 0

        for i in range(n):

            while j < n and nums[j] <= k * nums[i]:
                j += 1
            ans = max(ans, (j - i))

        return n - ans
