class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minSum = float("inf")

        for i in range(n):
            for j in range(i, n):
                if l <= j - i + 1 <= r:
                    currSum = sum(nums[i : j + 1])
                    if currSum > 0:
                        minSum = min(minSum, currSum)

        return minSum if minSum != float("inf") else -1
