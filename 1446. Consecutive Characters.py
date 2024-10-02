class Solution:
    def maxPower(self, s: str) -> int:
        
        maximum = 0
        temp = 0

        for i in range(1, len(s)):    
            if s[i] == s[i - 1]:
                temp += 1
                maximum = max(maximum, temp)
            
            else:
                temp = 0
        
        return maximum + 1
