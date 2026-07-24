class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n == 2:
            return n

        ans = 1
        while ans <= n:
            ans *= 2

        return ans
