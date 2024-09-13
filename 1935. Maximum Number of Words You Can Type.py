class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        texts = text.split(' ')
        ans = 0

        for text in texts:
            can_type = True

            for char in brokenLetters:
                if char in text:
                    can_type = False
                    break
            if can_type:
                ans += 1
        
        return ans