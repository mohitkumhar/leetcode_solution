class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        n = len(nums)

        i = 0
        j = 0

        pairs = 0
        result = 0
        freq = {}

        while j < n:

            pairs += freq.get(nums[j], 0)
            freq[nums[j]] = freq.get(nums[j], 0) + 1

            while pairs >= k:
                result += n - j
                freq[nums[i]] = freq.get(nums[i], 0) - 1
                pairs -= freq[nums[i]]

                i += 1
            j += 1

        return result
