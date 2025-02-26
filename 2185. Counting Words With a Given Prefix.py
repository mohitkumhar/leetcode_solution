class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        p_len = len(pref)
        ans = 0
        for word in words:
            if word[:p_len] == pref:
                ans += 1
        
        return ans

