class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        map = {'a': 0, 'b': 0, 'c': 0}
        result = 0
        left = 0


        for right in range(len(s)):
            
            map[s[right]] += 1
        
            while all(map[char] > 0 for char in 'abc'):
                result += len(s) - right

                map[s[left]] -= 1
                left += 1
        
        return result
