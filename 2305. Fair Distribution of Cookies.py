class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        n = len(cookies)
        children = [0] * (k + 1)
        self.ans = float('inf')

        def solve(i):
            if i == n:
                self.ans = min(self.ans, max(children))
                return
            
            for j in range(k):
                children[j] += cookies[i]
                solve(i + 1)
                children[j] -= cookies[i]
                
                if children[j] == 0:
                    break
            
        
        solve(0)
        return self.ans



        
