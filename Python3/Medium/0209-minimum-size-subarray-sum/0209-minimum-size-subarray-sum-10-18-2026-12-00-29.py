class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        i = 0
        j = 0

        ans = float("inf")
        n = len(nums)

        currSum = 0

        while j < n:
            currSum += nums[j]

            while currSum >= target:
                ans = min(ans, j - i + 1)
                currSum -= nums[i]
                i += 1
            j += 1

        return ans if ans != float("inf") else 0
