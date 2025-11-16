class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        start = 0
        end = 0
        n = len(nums)

        for i, num in enumerate(nums):
            if num < nums[start]:
                start = i
            if num > nums[end]:
                end = i

        if start < end:
            return start + (n-end-1)
        return start + (n-end-1) - 1
