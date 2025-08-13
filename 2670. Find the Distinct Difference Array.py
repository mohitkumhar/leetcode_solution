class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        distinct = []
        for i in range(len(nums)):
            left = len(set(nums[:i + 1]))
            right = len(set(nums[i + 1:]))
            distinct.append(left - right)
        return distinct
