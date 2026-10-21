class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""

        minChar = min(strs)
        minCharLen = len(minChar)

        for i in range(minCharLen):
            currChar = minChar[i]

            for str in strs:
                if str[i] != currChar:
                    return ans

            ans += currChar

        return ans
