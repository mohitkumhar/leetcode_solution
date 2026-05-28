class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = {}
        last_lower = {}

        for index, char in enumerate(word):
            if char.islower():
                last_lower[char] = index
            else:
                first_upper.setdefault(char, index)

        count = 0

        for offset in range(26):
            lower = chr(ord("a") + offset)
            upper = chr(ord("A") + offset)

            if lower in last_lower and upper in first_upper and last_lower[lower] < first_upper[upper]:
                count += 1

        return count
