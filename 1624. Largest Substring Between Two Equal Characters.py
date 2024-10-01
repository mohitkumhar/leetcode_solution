class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = {}
        max_length = -1

        for i, char in enumerate(s):
            if char in count:

                length = i - count[char] - 1
                max_length = max(max_length, length)

            else:
                count[char] = i

        return max_length
