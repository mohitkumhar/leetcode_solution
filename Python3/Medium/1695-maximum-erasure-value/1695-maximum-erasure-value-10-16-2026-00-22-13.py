class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        counter = {}
        n = len(nums)

        i = 0
        j = 0

        ans = 0
        currSum = 0

        while j < n:

            counter[nums[j]] = counter.get(nums[j], 0) + 1
            currSum += nums[j]

            while counter[nums[j]] > 1:
                counter[nums[i]] -= 1
                currSum -= nums[i]
                i += 1

            ans = max(ans, currSum)
            j += 1

        return ans
