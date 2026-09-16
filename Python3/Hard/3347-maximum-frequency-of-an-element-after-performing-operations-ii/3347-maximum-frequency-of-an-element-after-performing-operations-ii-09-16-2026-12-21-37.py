class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        maxVal = max(nums) + k

        freq = {}
        events = {}

        for i in range(n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            left = max(nums[i] - k, 0)
            right = min(nums[i] + k, maxVal)

            events[nums[i]] = events.get(nums[i], 0) + 0
            events[left] = events.get(left, 0) + 1
            events[right + 1] = events.get(right + 1, 0) - 1

        result = 1
        cumSum = 0

        for key, value in sorted(events.items()):
            target = key
            value += cumSum

            targetFreq = freq.get(target, 0)
            maxPosFreq = min(value - targetFreq, numOperations)

            result = max(result, maxPosFreq + targetFreq)

            cumSum = value

        return result
