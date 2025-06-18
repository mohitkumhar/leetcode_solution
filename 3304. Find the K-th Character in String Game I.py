class Solution:
    def kthCharacter(self, k: int) -> str:
        words = 'a'
        while len(words) < k:
            for word in words:
                words += chr(ord(word) + 1)

        return words[k - 1]
