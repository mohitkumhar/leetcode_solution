class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        i = 0
        j = 0

        currVowelCount = 0
        vowel = set("aeiou")

        n = len(s)
        ans = 0

        while j < n:
            if s[j] in vowel:
                currVowelCount += 1
                ans = max(ans, currVowelCount)

            if j - i + 1 < k:
                j += 1

            elif j - i + 1 == k:
                if s[i] in vowel:
                    currVowelCount -= 1
                i += 1
                j += 1

        return ans
