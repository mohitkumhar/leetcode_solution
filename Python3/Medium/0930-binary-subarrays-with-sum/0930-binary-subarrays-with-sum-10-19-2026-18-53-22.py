class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        n = len(nums)

        def helper(goal):
            if goal < 0:
                return 0

            i = 0
            j = 0

            currSum = 0
            ans = 0

            while j < n:
                currSum += nums[j]

                while currSum > goal:
                    currSum -= nums[i]
                    i += 1

                ans += j - i + 1
                j += 1

            return ans

        return helper(goal) - helper(goal - 1)
