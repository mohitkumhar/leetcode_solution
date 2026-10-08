class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        def solve(s1, s2):
            if s1 == s2:
                return True
            if len(s1) != len(s2):
                return False

            key = s1 + "_" + s2

            if key in memo:
                return memo[key]

            n = len(s1)
            result = False

            for i in range(1, n):
                swapped = solve(s1[i:], s2[: n - i]) and solve(s1[:i], s2[n - i :])
                notSwapped = solve(s1[i:], s2[i:]) and solve(s1[:i], s2[:i])

                if swapped or notSwapped:
                    result = True
                    break

            memo[key] = result
            return memo[key]

        memo = {}

        return solve(s1, s2)
