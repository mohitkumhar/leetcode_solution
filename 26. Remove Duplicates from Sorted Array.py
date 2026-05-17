class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0 
        n = len(nums)

        while j < n and i < n:
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]

        return i + 1
