class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        for i in range(len(nums)):
            leftSum = max(nums[: i + 1])
            rightSum = min(nums[i:])

            if (leftSum - rightSum) <= k:
                return i

        return -1
