class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def backtrack(i, j, currWord):
            if j >= n:
                result.append(" ".join(currWord))
                return

            for j in range(n):
                if s[i : j + 1] in wordDict:
                    currWord.append(s[i : j + 1])
                    backtrack(j + 1, j + 1, currWord)
                    currWord.pop()

        n = len(s)
        result = []

        wordDict = set(wordDict)

        backtrack(0, 0, [])

        return result
