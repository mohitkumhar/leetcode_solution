class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        i = 0
        j = 0
        n = len(fruits)
        count = 0
        ans = 0
        freq = {}

        while j < n:
            if fruits[j] not in freq:
                count += 1

            freq[fruits[j]] = freq.get(fruits[j], 0) + 1

            while i < n and count > 2:
                freq[fruits[i]] = freq.get(fruits[i], 0) - 1
                if freq[fruits[i]] == 0:
                    del freq[fruits[i]]

                    count -= 1
                i += 1
            ans = max(ans, j - i + 1)
            j += 1

        return ans
