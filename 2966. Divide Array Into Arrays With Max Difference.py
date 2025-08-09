class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(0, len(nums), 3):
            group = nums[i: i+3]
            if (group[-1] - group[0]) > k:
                return []
            result.append(group)
        return result