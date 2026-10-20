class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        s1Freq = [0] * 26
        s2Freq = [0] * 26

        for char in s1:
            s1Freq[ord(char) - ord("a")] += 1

        i = 0
        j = 0

        while j < m:
            s2Freq[ord(s2[j]) - ord("a")] += 1

            if j - i + 1 < n:
                j += 1

            elif j - i + 1 == n:
                if s1Freq == s2Freq:
                    return True

                s2Freq[ord(s2[i]) - ord("a")] -= 1
                i += 1
                j += 1

        return False
