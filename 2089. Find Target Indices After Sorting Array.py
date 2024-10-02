class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        ans = []
        index = 0

        for i in sorted_nums:
            if i == target:
                ans.append(index)
            index+=1
            
        return ans
