class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        numDict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in numDict:
                return [numDict[complement], i]

            numDict[num] = i
