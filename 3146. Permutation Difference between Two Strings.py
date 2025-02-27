class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        map = {}

        for i in range(len(t)):
            map[t[i]] = i

        sum = 0
        for i in range(len(s)):
            sum += abs(i - map[s[i]])

        return sum
