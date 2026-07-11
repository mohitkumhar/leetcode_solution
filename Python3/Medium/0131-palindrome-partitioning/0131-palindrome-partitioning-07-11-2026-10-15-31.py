class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def solve(i, curr_part):
            if i == len(s):
                result.append(curr_part[:])
                return 

            for j in range(i, len(s)):
                if dp[i][j] == True:
                    curr_part.append(s[i:j + 1])
                    solve(j + 1, curr_part)
                    curr_part.pop()
            
        


        n = len(s)
        dp = [[True for _ in range(n + 1)] for _ in range(n + 1)]

        for L in range(1, n + 1):
            i = 0
            while (i + L - 1) < n:
                j = i + L - 1

                if L == 1:
                    dp[i][j] = True
                elif L == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1] == True

                i += 1

        result = []

        solve(0, [])
        return result


