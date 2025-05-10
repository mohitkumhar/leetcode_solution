class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0

        for num in nums:
            count += num
            ans.append(count)
        
        return ans
