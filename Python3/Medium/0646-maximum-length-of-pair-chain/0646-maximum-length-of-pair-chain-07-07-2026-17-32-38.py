class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)

        memo = [[-1 for _ in range(n)] for _ in range(n)]

        def solve(idx, prev):
            if idx >= n:
                return 0
            if memo[idx][prev] != -1:
                return memo[idx][prev]

            skip = solve(idx + 1, prev)

            take = skip
            if prev == -1 or pairs[prev][1] < pairs[idx][0]:
                take = 1 + solve(idx + 1, idx)

            memo[idx][prev] = max(take, skip)
            return memo[idx][prev]

        return solve(0, -1)
