class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 4:
            return 0

        nums.sort()

        case_1 = nums[-4] - nums[0]

        case_2 = nums[-3] - nums[1]

        case_3 = nums[-2] - nums[2]

        case_4 = nums[-1] - nums[3]

        return min(case_1, case_2, case_3, case_4)
