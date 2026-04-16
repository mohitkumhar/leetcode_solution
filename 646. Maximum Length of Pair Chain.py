class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def solve(idx, prev):
            if idx >= n:
                return 0
            if memo[idx][prev] != -1:
                return memo[idx][prev]

            skip = solve(idx + 1, prev)

            take = 0
            if prev == -1 or pairs[prev][1] < pairs[idx][0]:
                take = 1 + solve(idx + 1, idx)
            ans = max(take, skip)
            memo[idx][prev] = ans
            return ans

        return solve(0, -1)
