class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        nums.sort()
        expected = list(range(1, n))
        expected2 = expected[:]

        expected2.append(n-1)

        return nums == expected or nums == expected2
