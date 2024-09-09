class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        value = 0

        for num in nums:
            value = (value * 2 + num)

            if value % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans