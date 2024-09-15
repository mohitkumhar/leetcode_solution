class Solution:
    def greatestLetter(self, s: str) -> str:
        s_set = set(s)
        ans = ''

        s = ''.join(sorted(s, reverse=True))

        for char in s:
            if char.upper() in s_set and char.lower() in s_set:
                ans = char.upper()
                break
            
        return ans
        