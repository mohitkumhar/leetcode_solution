class Solution:
    def minOperations(self, s: str) -> int:
        sorted = True
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                sorted = False
                break
        if sorted:
            return 0
        
        if len(s) == 2:
            return -1

        mi = min(s)
        mx = max(s)

        if s[0] == mi or s[-1] == mx:
            return 1
        
        for i in range(1, len(s) - 1):
            if s[i] == mi or s[i] == mx:
                return 2
        return 3







