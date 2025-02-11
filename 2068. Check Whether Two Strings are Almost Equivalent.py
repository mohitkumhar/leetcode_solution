class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        map = {}

        for char in word1:
            if char in map:
                map[char] += 1
            
            else:
                map[char] = 1

        for char in word2:
            if char in map:
                map[char] -= 1
            
            else:
                map[char] = -1
        
        if any(val < -3 or val > 3 for val in map.values()):
            return False
        
        return True

        