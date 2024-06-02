class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        odd = []

        for i in nums:
            if i % 2 == 0:
                ans.append(i)

            else:
                odd.append(i)

        return ans + odd
