class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * (n+1)
        max_val=0
        prev_idx = [-1] * (n + 1)
        last_chosen_idx = -1

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev_idx[i] = j
                    
            if dp[i] > max_val:
                max_val = dp[i]
                last_chosen_idx = i

        result = []

        while last_chosen_idx != -1:
            result.append(nums[last_chosen_idx])
            last_chosen_idx = prev_idx[last_chosen_idx]

        print(result)
        return result
