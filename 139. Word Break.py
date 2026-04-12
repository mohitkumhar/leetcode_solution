class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        n = len(s)

        for i in range(n+1):
            for j in range(0, i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True

        return dp[n]
        
