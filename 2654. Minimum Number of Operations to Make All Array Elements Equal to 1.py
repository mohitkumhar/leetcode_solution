class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones > 0:
            return n - ones

        ans = float('inf')

        for i in range(n):
            g = nums[i]
            for j in range(i+1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    ans = min(ans, j - i)
                    break

        if ans == float('inf'):
            return -1
        return ans + n - 1
