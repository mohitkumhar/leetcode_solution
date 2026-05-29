class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        counter = {}
        i = 0
        ans_idx = []

        for char in p:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1
        count = len(counter)
        original_counter = counter.copy()

        for j in range(n):

            if s[j] in counter:
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    count -= 1
                while counter[s[j]] < 0:
                    if counter[s[i]] == 0:
                        count += 1
                    counter[s[i]] += 1
                    i += 1
            else:
                counter = original_counter.copy()
                count = len(counter)
                i = j + 1

            if not count:
                ans_idx.append(i)
                if counter[s[i]] == 0:
                    count += 1
                counter[s[i]] += 1

                i += 1

        return ans_idx
