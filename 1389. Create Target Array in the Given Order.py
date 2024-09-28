class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []

        for ind, num in zip(index, nums):
            ans.insert(ind, num)
            
        
        return ans
             
        