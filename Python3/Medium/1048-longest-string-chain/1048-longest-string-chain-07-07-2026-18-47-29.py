class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        def check_predecessor(str1: int, str2: int) -> bool:
            if (len(str1) - len(str2)) != 1:
                return False
            i = 0
            j = 0
            diff = 0

            while i < len(str2):
                if str2[i] == str1[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    diff += 1
                    if diff >= 2:
                        return False
            return True

        def solve(idx, prev):
            if idx >= n:
                return 0
            if memo[idx][prev] != -1:
                return memo[idx][prev]

            skip = solve(idx + 1, prev)
            take = skip
            if prev == -1 or check_predecessor(words[idx], words[prev]):
                take = 1 + solve(idx + 1, idx)

            memo[idx][prev] = max(take, skip)
            return memo[idx][prev]

        n = len(words)
        memo = [[-1 for _ in range(n)] for _ in range(n)]
        return solve(0, -1)
