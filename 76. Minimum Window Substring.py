class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        n = len(s)
        freq = {}
        count = len(t)
        min_length = float('inf')

        for char in t:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1



        for j in range(n):

            if s[j] in freq:
                if freq[s[j]] > 0:
                    count -= 1
                freq[s[j]] -= 1


            while count == 0:

                if j - i + 1 < min_length:
                    min_length = j - i + 1
                    temp = i

                if s[i] in freq:
                    freq[s[i]] += 1
                    if freq[s[i]] > 0:
                        count += 1

                i += 1
        return "" if min_length == float('inf') else s[temp:temp + min_length]
