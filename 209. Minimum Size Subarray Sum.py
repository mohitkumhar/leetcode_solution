class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        start = 0
        current_sum = 0

        min_sub = float('inf')

        for end in range(len(nums)):
            current_sum += nums[end]

            while current_sum >= target:
                min_sub = min(min_sub, end - start + 1)
                current_sum -= nums[start]
                start += 1
        
        return 0 if min_sub == float('inf') else min_sub
