class Solution:
    def canJump(self, nums: list[int]) -> bool:
        
        maxReachable = 0
        n = len(nums)

        for i in range(n):
            if i > maxReachable:
                return False
            if i == n - 1:
                return True
            
            maxReachable = max(maxReachable, i + nums[i])
        