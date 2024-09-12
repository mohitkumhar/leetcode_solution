class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        ans = 0

        for word in words:
            continous = True
            for char in word:
                if not char in allowed_set:
                    continous = False
                    break
            
            if continous:
                ans += 1
        
        return ans
