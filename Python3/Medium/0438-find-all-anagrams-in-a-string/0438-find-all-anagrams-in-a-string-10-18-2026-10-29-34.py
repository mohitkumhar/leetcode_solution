class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []

        counter = {}

        for char in p:
            counter[char] = counter.get(char, 0) + 1

        i = 0
        j = 0

        k = len(p)
        p = set(p)

        n = len(s)

        while j < n:

            if s[j] in p:
                counter[s[j]] = counter.get(s[j], 0) - 1
                if counter[s[j]] == 0:
                    del counter[s[j]]

            if (j - i + 1) < k:
                j += 1

            elif (j - i + 1) == k:
                if not counter:
                    result.append(i)

                if s[i] in p:
                    counter[s[i]] = counter.get(s[i], 0) + 1
                    if counter[s[i]] == 0:
                        del counter[s[i]]

                i += 1
                j += 1

        return result
