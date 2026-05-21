class Solution:
    def longestBalanced(self, s: str) -> int:
        i = 0
        j = 0
        counter = {}
        n = len(s)
        ans = 0

        for i in range(n):
            j = i
            while j < n:
                idx = ord(s[j]) - 96
                
                if idx not in counter:
                    counter[idx] = 0
                counter[idx] += 1

                j += 1
                if len(set(counter.values())) == 1:
                    ans = max(ans, j - i)

            counter = {}

        return ans
