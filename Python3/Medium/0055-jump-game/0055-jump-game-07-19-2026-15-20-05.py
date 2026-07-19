class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reachable = 0
        n = len(nums)

        for i in range(n):
            if i > max_reachable:
                return False
            if i == n - 1:
                return True
            max_reachable = max(max_reachable, i + nums[i])

        return True
