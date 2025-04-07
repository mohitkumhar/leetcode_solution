class Solution:
    def addMinimum(self, word: str) -> int:
        expected = ['a', 'b', 'c']
        i = 0
        j = 0

        insertion = 0

        while i < len(word):
            if word[i] == expected[j]:
                i += 1
            
            else:
                insertion += 1
            
            j = (j + 1) % 3
        
        insertion += (3 - j) % 3
    
        return insertion
