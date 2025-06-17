class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0]
        rightSum = []
        left = 0
        right = 0

        for i in range(1, n):
            left += nums[i - 1]
            right += nums[n - i]

            leftSum.append(left)
            rightSum.insert(0, right)
        rightSum.append(0)

        result = []
        for i in range(n):
            result.append(abs(leftSum[i] - rightSum[i]))

        return result