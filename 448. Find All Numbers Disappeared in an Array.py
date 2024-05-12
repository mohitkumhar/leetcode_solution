class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])

        result = []

        for i, n in enumerate(nums):
            if n > 0:
                result.append(i + 1)
        
        return result

        