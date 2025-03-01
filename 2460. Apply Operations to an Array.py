class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        zeros = 0
        result = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                result.append(num)
        
        return result + [0] * zeros
