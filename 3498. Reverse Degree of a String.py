class Solution:
    def reverseDegree(self, s: str) -> int:
        char = 'a'
        index = 26
        map = {}
        while index != 0:
            map[char] = index
            index -= 1
            char = chr(ord(char) + 1)
        
        ans = 0
        for i in range(len(s)):
            ans += map[s[i]] * (i + 1)

        return ans