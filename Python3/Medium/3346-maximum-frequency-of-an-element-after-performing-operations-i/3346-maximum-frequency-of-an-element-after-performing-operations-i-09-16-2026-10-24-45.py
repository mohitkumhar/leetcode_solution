class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxVal = max(nums)
        freq = {}
        diff = [0] * (maxVal + 2)

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            l = max(nums[i] - k, 0)
            r = min(nums[i] + k, maxVal)

            diff[l] += 1
            diff[r + 1] -= 1

        result = 1

        for target in range(maxVal + 1):
            if target > 0:
                diff[target] += diff[target - 1]
            else:
                diff[target] += 0

            targetFreq = freq.get(target, 0)
            needConversion = diff[target] - targetFreq

            maxPossibleFreq = min(needConversion, numOperations)

            result = max(result, targetFreq + maxPossibleFreq)

        return result
