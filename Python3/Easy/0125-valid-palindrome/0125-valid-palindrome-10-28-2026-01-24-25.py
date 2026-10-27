class Solution:
    def isPalindrome(self, s: str) -> bool:
        validS = ""

        for char in s:
            if char.isalnum():
                validS += char.lower()

        return validS == validS[::-1]
