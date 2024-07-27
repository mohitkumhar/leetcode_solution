class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        m = 0
        n = len(s)
        ans = []

        for i in s:
            if i == 'I':
                ans.append(m)
                m += 1
            
            else:
                ans.append(n)
                n -= 1
        
        ans.append(n)
            
        return ans
        