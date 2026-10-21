class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            if nums[i] % 2 != 0 or nums[i] > threshold:
                continue

            for j in range(i, n):
                if nums[j] > threshold:
                    break

                if j > i and nums[j] % 2 == nums[j - 1] % 2:
                    break

                ans = max(ans, j - i + 1)

        return ans
