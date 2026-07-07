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

        n = len(words)

        dp = [1] * n
        count = 1
        for i in range(n):
            for j in range(i):
                if check_predecessor(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    count = max(count, dp[i])
        return count