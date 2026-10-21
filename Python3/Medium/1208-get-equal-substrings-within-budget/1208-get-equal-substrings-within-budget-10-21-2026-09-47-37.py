class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diffArray = []

        for i in range(len(s)):
            diff = abs(ord(s[i]) - ord(t[i]))
            diffArray.append(diff)

        i = 0
        j = 0
        currCost = 0
        ans = 0

        while j < n:
            currCost += diffArray[j]

            while currCost > maxCost:
                currCost -= diffArray[i]
                i += 1

            ans = max(ans, j - i + 1)

            j += 1

        return ans
