class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        result = [-1] * n

        if 2 * k + 1 > n:
            return result

        left = 0
        right = 2 * k + 1

        windowSum = 0

        for i in range(left, right):
            windowSum += nums[i]

        i = k
        windowLength = 2 * k + 1

        result[i] = windowSum // windowLength

        i += 1

        while right < n:
            outOfTheWindow = nums[left]
            comeToTheWindow = nums[right]

            windowSum = windowSum + comeToTheWindow - outOfTheWindow

            result[i] = windowSum // windowLength

            i += 1
            right += 1
            left += 1

        return result
