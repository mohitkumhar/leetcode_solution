class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        leftMultiply = []
        currLeftMulti = 1
        for num in nums:
            currLeftMulti *= num
            leftMultiply.append(currLeftMulti)

        rightMultiply = []
        currRightMulti = 1

        for i in range(len(nums) - 1, -1, -1):
            currRightMulti *= nums[i]
            rightMultiply.append(currRightMulti)
        rightMultiply = rightMultiply[::-1]

        result = []
        for i in range(len(nums)):
            leftMulti = leftMultiply[i - 1] if i > 0 else 1
            rightMulti = rightMultiply[i + 1] if i < n - 1 else 1

            currVal = leftMulti * rightMulti
            result.append(currVal)

        return result
