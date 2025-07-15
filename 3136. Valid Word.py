class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = set('aeiou')
        is_vowel = False
        is_cons = False

        for char in word:
            if not char.isalnum():
                return False

            if char.isalpha():
                if char.lower() in vowel:
                    is_vowel = True
                else:
                    is_cons = True

        return is_vowel and is_cons
