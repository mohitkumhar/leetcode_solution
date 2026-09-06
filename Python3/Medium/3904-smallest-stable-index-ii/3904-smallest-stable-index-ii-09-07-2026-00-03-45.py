class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        rightMin = [0] * n
        rightMin[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            rightMin[i] = min(rightMin[i + 1], nums[i])

        left = 0

        for i in range(n):
            left = max(left, nums[i])
            diff = left - rightMin[i]

            if diff <= k:
                return i

        return -1
