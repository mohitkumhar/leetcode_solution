class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for char in s:
            if char.isalpha() or char.isdigit():
                word += char.lower()

        i = 0
        j = len(word) - 1

        flag = False

        while i < j:
            if word[i] != word[j]:
                return False

            i += 1
            j -= 1

        return True
