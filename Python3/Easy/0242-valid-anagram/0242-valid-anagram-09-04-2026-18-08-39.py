class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}

        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1

            freq[t[i]] = freq.get(t[i], 0) - 1

            if freq.get(s[i], None) == 0:
                del freq[s[i]]
            if freq.get(t[i], None) == 0:
                del freq[t[i]]
        
        return len(freq) == 0