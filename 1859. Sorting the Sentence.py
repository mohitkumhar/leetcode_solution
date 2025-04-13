class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        result = [''] * (len(s) + 1)
        
        for word in s:
            result[int(word[-1])] = word[:-1]
        
        return (' '.join(result))[1:]
