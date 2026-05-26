class Solution:
    def minWindow(self, s, p):
        n = len(s)
        i = 0
        ans = float("inf")
        result = ""

        counter = {}
        for char in p:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1

        count = len(counter)

        for j in range(n):
            if s[j] in counter:
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    count -= 1
                
            while count == 0:
                if (j - i + 1) < ans:
                    ans = j - i + 1
                    result = s[i:j+1]

                if s[i] in counter:
                    counter[s[i]] += 1
                    if counter[s[i]] == 1:
                        count += 1
        
                i += 1

        return result
