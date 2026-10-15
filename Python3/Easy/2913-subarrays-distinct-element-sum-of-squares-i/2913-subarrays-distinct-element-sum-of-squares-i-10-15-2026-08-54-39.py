class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                count = len(set(nums[i : j + 1]))

                ans += count * count
        return ans
