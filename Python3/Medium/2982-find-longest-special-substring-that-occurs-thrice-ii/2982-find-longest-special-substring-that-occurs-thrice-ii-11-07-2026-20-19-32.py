class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        matrix = [[0 for _ in range(n + 1)] for _ in range(26)]

        currChar = s[0]
        currLen = 0

        for char in s:
            if char != currChar:
                currChar = char
                currLen = 0

            currLen += 1
            matrix[ord(char) - ord("a")][currLen] += 1

        ans = -1
        for i in range(26):
            cumSum = 0
            for j in range(n, -1, -1):
                cumSum += matrix[i][j]
                matrix[i][j] = cumSum

                if cumSum >= 3:
                    ans = max(ans, j)
                    break

        return ans
