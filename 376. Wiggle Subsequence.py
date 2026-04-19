class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[[-1 for _ in range(3)] for _ in range(n + 1)] for _ in range(n + 1)]

        # ' ' = 0
        # '+' = 1
        # '-' = 2

        def solve(idx, prev, prev_sign):
            if idx == n:
                return 0
            if memo[idx][prev][prev_sign] != -1:
                return memo[idx][prev][prev_sign]

            take = 0
            if prev == -1:
                take = 1 + solve(idx + 1, idx, 0)
            else:
                if (nums[idx] - nums[prev] < 0 and prev_sign != 2):
                    take = 1 + solve(idx + 1, idx, 2)

                elif (nums[idx] - nums[prev] > 0 and prev_sign != 1):
                    take = 1 + solve(idx + 1, idx, 1)

            skip = solve(idx + 1, prev, prev_sign)

            ans = max(take, skip)
            memo[idx][prev][prev_sign] = ans

            return ans

        return solve(0, -1, 0)
