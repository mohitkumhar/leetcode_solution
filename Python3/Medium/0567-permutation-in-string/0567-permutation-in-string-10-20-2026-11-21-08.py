class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        s1 = "".join(sorted(s1))

        for i in range(m - n + 1):
            subString = s2[i : i + n]

            if "".join(sorted(subString)) == s1:
                return True
        return False
