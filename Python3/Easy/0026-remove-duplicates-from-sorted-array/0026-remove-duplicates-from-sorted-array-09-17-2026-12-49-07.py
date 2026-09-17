class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        k = 0

        while i < n and k < n:
            if nums[k] == nums[i]:
                i += 1

            else:
                k += 1
                nums[k] = nums[i]

        return k + 1
