class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            count += min(nums[i] % 3, 3 - (nums[i] % 3))
        
        return count
