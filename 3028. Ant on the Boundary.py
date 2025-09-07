class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for num in nums:
            count += num
            if count == 0:
                ans += 1
        return ans