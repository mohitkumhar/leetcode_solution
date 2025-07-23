class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_cost = float('inf')
        n = len(nums)

        for i in range(1, n - 1):
            for j in range(i + 1, n):
                cost = nums[0] + nums[i] + nums[j]
                min_cost = min(min_cost, cost)
        return min_cost