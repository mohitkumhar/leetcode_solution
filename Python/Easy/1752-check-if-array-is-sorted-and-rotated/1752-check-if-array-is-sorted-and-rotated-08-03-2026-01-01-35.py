class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        rotation = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                rotation += 1

            if rotation >= 2:
                return False

        return True