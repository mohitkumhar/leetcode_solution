class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)

        max_prod = nums[0]

        left_multi = 1
        right_multi = 1

        for i in range(n):
            left_multi = left_multi * nums[i]
            right_multi = right_multi * nums[n - 1 - i]

            max_prod = max(max_prod, left_multi, right_multi)

            left_multi = left_multi if left_multi != 0 else 1
            right_multi = right_multi if right_multi != 0 else 1

        return max_prod
