class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        target = len(nums) // 3.0
        ans = []
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        for key, value in counter.items():
            if value > target:
                ans.append(key)
        
        return ans
        