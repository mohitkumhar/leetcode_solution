class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        n = len(strs)
        minWord = min(len(s) for s in strs)

        for i in range(minWord):
            currChar = strs[0][i]

            for s in strs:
                if s[i] == currChar:
                    continue
                else:
                    return strs[0][:i]
        return strs[0][:minWord]
