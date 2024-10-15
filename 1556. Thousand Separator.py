class Solution:
    def thousandSeparator(self, n: int) -> str:

        n_str = str(n)
        
        if len(n_str) < 4:
            return n_str
        
        n_str = n_str[::-1]

        result = ''

        for i in range(len(n_str) - 1, -1, -1):
            result += n_str[i]
            if i % 3 == 0:
                result += '.'
            
        
        return result[:-1]
