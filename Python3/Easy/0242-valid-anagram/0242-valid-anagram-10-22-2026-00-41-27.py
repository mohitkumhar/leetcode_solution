class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in t:
            freq[char] = freq.get(char, 0) - 1
            if freq[char] == 0:
                del freq[char]

        return len(freq) == 0
