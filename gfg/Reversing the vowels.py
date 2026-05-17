#User function Template for python3

class Solution:
    def modify(self, s):
        n = len(s)
        i = 0
        j = n - 1
        s = list(s)
        vowel = set('aeiou')
        
        while i < j:
            if s[i] in vowel and s[j] in vowel:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
            if i < j and s[i] not in vowel:
                i += 1
            
            if i < j and s[j] not in vowel:
                j -= 1
        
        return ''.join(s)
            
        
