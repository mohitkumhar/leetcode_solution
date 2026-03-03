class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for num in nums:
            temp = 0
            for i in str(num):
                temp += int(i)

            result.append(temp)
        return min(result)
