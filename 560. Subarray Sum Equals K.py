class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        current_sum = 0
        prefix_sum = {0: 1}

        for i in range(len(nums)):

            current_sum += nums[i]

            if current_sum - k in prefix_sum:
                result += prefix_sum[current_sum - k]
            
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return result   
