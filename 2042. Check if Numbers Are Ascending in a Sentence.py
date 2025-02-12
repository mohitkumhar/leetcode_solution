class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        s = [int(i) for i in s.split() if i.isdigit()]

        for i in range(1, len(s)):
            if s[i - 1] >= s[i]:
                return False
        
        return True
