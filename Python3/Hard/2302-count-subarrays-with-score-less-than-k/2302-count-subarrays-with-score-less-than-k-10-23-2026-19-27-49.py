class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        i = 0
        j = 0

        currSum = 0
        count = 0

        while j < n:
            currSum += nums[j]

            currProd = currSum * (j - i + 1)

            while i <= j and currProd >= k:
                currSum -= nums[i]
                i += 1
                currProd = currSum * (j - i + 1)
            count += j - i + 1
            j += 1

        return count
