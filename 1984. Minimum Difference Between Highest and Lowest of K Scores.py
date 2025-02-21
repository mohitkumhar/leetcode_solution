class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        min_diff = float('inf')
        
        for start in range(len(nums) - k + 1):
            diff = nums[start + k - 1] - nums[start]

            min_diff = min(min_diff, diff)
            
        return min_diff
