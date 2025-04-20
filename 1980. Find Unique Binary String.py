
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        ans = ''

        for i in range(len(nums)):
            if nums[i][i] == '1':
                ans += '0'
            else:
                ans += '1'
        
        return ans
