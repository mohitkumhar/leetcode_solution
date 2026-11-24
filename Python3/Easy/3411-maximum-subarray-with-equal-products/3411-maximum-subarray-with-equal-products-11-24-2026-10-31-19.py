class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                gcd = math.gcd(*nums[i:j + 1])
                lcm = math.lcm(*nums[i:j + 1])
            
                if prod == (gcd * lcm):
                    ans = max(ans, j - i + 1)

        return ans
