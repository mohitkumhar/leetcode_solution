class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        sum = nums[0]
        temp = nums[0]

        for i in range(1, len(nums)):

            
            if nums[i - 1] < nums[i]:
                temp += nums[i]
            
            else:
                sum = max(sum, temp)
                temp = nums[i]

            sum = max(sum, temp)

        return sum
