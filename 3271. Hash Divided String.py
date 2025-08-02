class Solution:
    def stringHash(self, s: str, k: int) -> str:

        def hashedChar(string):
            temp = 0
            for char in string:
                index = ord(char.lower()) - ord('a')
                temp += index
            return temp

        n = len(s)
        parts = []
        for i in range(0, n, k):
            parts.append(s[i: i + k])

        ans = ''
        for part in parts:
            hash_score = hashedChar(part)

            index = hash_score % 26
            char = chr(index + ord('a'))
            ans += char

        return ans