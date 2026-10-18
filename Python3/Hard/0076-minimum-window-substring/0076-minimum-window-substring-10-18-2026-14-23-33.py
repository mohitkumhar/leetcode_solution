class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        counter = {}

        for char in t:
            counter[char] = counter.get(char, 0) + 1

        i = 0
        j = 0
        k = len(t)
        ans = float("inf")
        result = ""

        count = len(counter)

        while j < n:
            if s[j] in t:
                counter[s[j]] = counter.get(s[j], 0) - 1

                if counter[s[j]] == 0:
                    count -= 1

            while count == 0:
                if (j - i + 1) < ans:
                    ans = j - i + 1
                    result = s[i : j + 1]

                if s[i] in counter:
                    counter[s[i]] += 1
                    if counter[s[i]] == 1:
                        count += 1

                i += 1
            j += 1

        return result
