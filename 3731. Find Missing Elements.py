class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        nums = sorted(nums)

        for i in range(nums[0], nums[-1]):
            if i not in nums:
                ans.append(i)
        return ans
