class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicate = 0
        seen = set()
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        missing = -1

        for i in range(1, len(nums) + 1):
            if not i in seen:
                missing = i
            
        return [duplicate, missing]