class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(index, current):
            if index == len(nums):
                result.append(current)
                return
            
            helper(index + 1, current)
            helper(index + 1, current + [nums[index]])

        helper(0, [])
        return result
