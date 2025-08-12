class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for num in nums[0]:
            if all(num in i for i in nums):
                ans.append(num)
        return sorted(ans)