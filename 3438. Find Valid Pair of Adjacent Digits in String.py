class Solution:
    def findValidPair(self, s: str) -> str:
        counter = {}
        ans = ''
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        for i in range(1, len(s)):
            val1 = s[i-1]
            val2 = s[i]
            if val1 != val2:
                if counter[val1] == int(val1) and counter[val2] == int(val2):
                    ans = val1+val2
                    break
        return ans if ans else ''
