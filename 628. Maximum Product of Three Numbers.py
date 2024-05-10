class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)

        sort_nums = sorted(nums)

        min1 = sort_nums[0]
        min2 = sort_nums[1]

        max1 = sort_nums[length - 1]
        max2 = sort_nums[length - 2]
        max3 = sort_nums[length - 3]

        return max(min1 * min2 * max1, max1 * max2 * max3)
