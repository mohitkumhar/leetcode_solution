class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(char: str) -> int:

            best = 0
            left = 0
            flip = 0
            
            for right, ch in enumerate(answerKey):
                if ch != char:
                    flip += 1
                
                while flip > k:
                    if answerKey[left] != char:
                        flip -= 1
                    left += 1
            
                best = max(best, right - left + 1)
            
            return best
    
        return max(helper('T'), helper('F'))
