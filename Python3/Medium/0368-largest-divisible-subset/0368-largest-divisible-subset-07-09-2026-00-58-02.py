class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        dp = [1] * (n + 1)
        prev_idx = [-1] * (n + 1)
        count = 0
        max_seen_idx = -1

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < (dp[j] + 1):
                        dp[i] = dp[j] + 1
                        prev_idx[i] = j

            if dp[i] > count:
                count = dp[i]
                max_seen_idx = i

        result = []
        while max_seen_idx != -1:
            result.append(nums[max_seen_idx])
            max_seen_idx = prev_idx[max_seen_idx]

        return result
