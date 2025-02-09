class Solution:
    def minimumMoves(self, s: str) -> int:
        
        ans = 0
        i = 0

        while i < len(s):
            
            if s[i] == 'X':
                i += 3
                ans += 1
                continue
            else:
                i += 1
            
        return ans
            

                

        