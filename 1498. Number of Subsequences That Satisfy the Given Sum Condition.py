class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        left = 0
        right = n - 1
        result = 0
        MOD = 10**9 + 7

        while left <= right:
            if (nums[left] + nums[right]) <= target:
                result = result + (2**(right - left))
                left += 1
            else:
                right -= 1

        return result % MOD
