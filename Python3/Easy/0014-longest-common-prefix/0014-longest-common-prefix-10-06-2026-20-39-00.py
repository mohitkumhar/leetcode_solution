class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        n = len(strs)
        minWord = min(s for s in strs)

        for i in range(n):
            currChar = strs[0][i]

            for s in strs:
                if s[i] == currChar:
                    continue
                else:
                    return strs[0][:i]
        return minWord
