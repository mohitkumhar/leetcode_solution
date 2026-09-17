class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        i = 0
        j = 0
        result = float("inf")
        bestMinIdx = float("inf")
        minBestLenTillIdx = [float("inf")] * n

        currSum = 0

        while j < n:
            currSum += arr[j]

            while i < j and currSum > target:
                currSum -= arr[i]
                i += 1

            if currSum == target:
                length = j - i + 1

                if i > 0 and minBestLenTillIdx[i - 1]:
                    result = min(result, minBestLenTillIdx[i - 1] + length)

                bestMinIdx = min(bestMinIdx, length)

            minBestLenTillIdx[j] = bestMinIdx
            j += 1

        return result if result != float("inf") else -1
