class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:

        maxKPos = -1
        minKPos = -1
        culpritIdx = -1
        ans = 0

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                culpritIdx = i
            if nums[i] == minK:
                minKPos = i
            if nums[i] == maxK:
                maxKPos = i

            minValIdx = min(minKPos, maxKPos)
            tempAns = minValIdx - culpritIdx

            ans += tempAns if tempAns > 0 else 0

        return ans
