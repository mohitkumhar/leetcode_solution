class Solution:
    def countAsterisks(self, s: str) -> int:

        count = 0
        inside = False

        for char in s:
            if char == '|':
                if inside:
                    inside = False
                else:
                    inside = True
            
            elif char == '*' and not inside:
                count += 1
        
        return count
