class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []

        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
                break

        if len(ans) == 0:
            return [-1, -1]

        for j in reversed(range(len(nums))):
            if nums[j] == target:
                ans.append(j)
                break

        return ans
