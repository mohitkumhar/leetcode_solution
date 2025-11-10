class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = float('inf')
        freq = {}
        for char in text:
            freq[char] = freq.get(char, 0) + 1
        required = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}

        for char, need in required.items():
            if char not in freq:
                return 0

            count = min(count, freq[char] // need)

        return count
