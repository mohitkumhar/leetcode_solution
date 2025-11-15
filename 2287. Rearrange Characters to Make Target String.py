class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        target_freq = {}
        freq = {}

        for char in target:            
            target_freq[char] = target_freq.get(char, 0) + 1
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        count = float('inf')
        
        for item, value in target_freq.items():
            if item not in freq:
                return 0
            count = min(count, freq[item] // target_freq[item])
        
        return count
