class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n = len(words)
        memo = [[-1] * (n + 1) for _ in range(n + 1)]

        def check_predecessor(word1, word2):
            if (len(word1) - len(word2)) != 1:
                return False

            i = 0
            j = 0
            max_skip = 0

            while i < len(word2):
                if word2[i] == word1[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    max_skip += 1
                    if max_skip == 2:
                        return False
            return True

        def solve(idx, prev):
            if idx >= n:
                return 0
            if memo[idx][prev] != -1:
                return memo[idx][prev]

            skip = solve(idx + 1, prev)

            take = 0
            if prev == -1 or check_predecessor(words[idx], words[prev]):
                take = 1 + solve(idx + 1, idx)

            ans = max(skip, take)
            memo[idx][prev] = ans
            return ans

        return solve(0, -1)
