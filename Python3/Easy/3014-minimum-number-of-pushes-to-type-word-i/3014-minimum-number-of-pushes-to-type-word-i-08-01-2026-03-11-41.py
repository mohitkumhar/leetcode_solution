class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}

        assign_key = 2
        ans = 0

        for char in word:
            freq[assign_key] = freq.get(assign_key, 0) + 1
            ans += freq[assign_key]

            if assign_key == 9:
                assign_key = 2
            else:
                assign_key += 1

        return ans
