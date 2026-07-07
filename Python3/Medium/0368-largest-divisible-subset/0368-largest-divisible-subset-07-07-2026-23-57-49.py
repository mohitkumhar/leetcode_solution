class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        count = 0
        dp = [1 for _ in range(n)]
        prev_idx = [-1] * n
        last_choosen_idx = -1

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < (dp[j] + 1):
                        dp[i] = dp[j] + 1
                        prev_idx[i] = j

            if dp[i] > count:
                count = dp[i]
                last_choosen_idx = i

        result = []

        while last_choosen_idx != -1:
            result.append(nums[last_choosen_idx])
            last_choosen_idx = prev_idx[last_choosen_idx]

        return result
