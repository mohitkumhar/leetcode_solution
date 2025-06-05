class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def palindrom(string):
            if string[::-1] == string:
                return True
            return False

        for word in words:
            if palindrom(word):
                return word
        
        return ""