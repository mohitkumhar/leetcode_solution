class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = 0
        n = len(nums)
        ans = 0
        freq = {}

        for j in range(n):
            if nums[j] not in freq:
                freq[nums[j]] = 0
            freq[nums[j]] += 1

            while freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)

        return ans
