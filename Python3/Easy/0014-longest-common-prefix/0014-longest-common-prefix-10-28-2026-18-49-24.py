class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""

        minPrefix = min(strs)
        i = 0

        for char in minPrefix:

            for word in strs:

                if i < len(word) and word[i] == char:
                    continue
                else:
                    return minPrefix[:i]
            i += 1

        return minPrefix
