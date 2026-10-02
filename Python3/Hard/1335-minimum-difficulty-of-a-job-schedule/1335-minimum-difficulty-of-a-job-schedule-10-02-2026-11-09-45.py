class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:

        if len(jobDifficulty) < d:
            return -1

        def solve(idx, day):
            if day == 1:
                return max(jobDifficulty[idx:])

            if (idx, day) in memo:
                return memo[(idx, day)]

            maxDay = float("-inf")
            finalResult = float("inf")

            for i in range(idx, len(jobDifficulty) - (day - 1)):
                maxDay = max(maxDay, jobDifficulty[i])
                result = maxDay + solve(i + 1, day - 1)

                finalResult = min(finalResult, result)

            memo[(idx, day)] = finalResult
            return finalResult

        memo = {}
        return solve(0, d)
