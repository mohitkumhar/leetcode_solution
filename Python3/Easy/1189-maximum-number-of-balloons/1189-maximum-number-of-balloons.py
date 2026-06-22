class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        req_map = {}
        for char in "balloon":
            req_map[char] = req_map.get(char, 0) + 1

        freq = {}
        for char in text:
            freq[char] = freq.get(char, 0) + 1
        
        min_count = float('inf')
        for char, need in req_map.items():
            if char not in freq:
                return 0
            
            min_count = min(min_count, freq[char] // need)
        
        return min_count
