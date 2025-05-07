class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        s = ['1', '2', '2']
        index = 2
        next_char = '1'

        while len(s) < n:
            count = int(s[index])
            s.extend([next_char] * count)
            next_char = '1' if next_char == '2' else '2'
            index += 1
        
        return s[:n].count('1')