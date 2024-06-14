class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        ans = 0
        prev = nums[0]

        for num in range(1, len(nums)):
            if nums[num] <= prev:
                ans = ans + (prev + 1 - nums[num])
                prev += 1

            else:
                prev = nums[num]

        return ans
