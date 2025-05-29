class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            if nums[i - 1] != nums[i]:
                if i != len(nums) - 1 and nums[i] != nums[i + 1]:
                    return nums[i]

                if i == len(nums) - 1:
                    return nums[i]
