class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {char: 0 for char in order}

        for char in s:
            if char in count:
                count[char] += 1

        result = ''

        for char in order:
            result += char * count[char]
        for char in s:
            if char not in order:
                result += char

        return result