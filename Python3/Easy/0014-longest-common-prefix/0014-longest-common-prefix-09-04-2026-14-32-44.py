class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minWordLen = min(len(s) for s in strs)

        for i in range(minWordLen):
            currChar = strs[0][i]

            if all(s[i] == currChar for s in strs):
                continue

            else:
                return strs[0][:i]

        return strs[0][:minWordLen]
