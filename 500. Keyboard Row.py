class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        result = []

        for word in words:
            lower_case_word = word.lower()
            if all(char in row1 for char in lower_case_word) or \
               all(char in row2 for char in lower_case_word) or \
               all(char in row3 for char in lower_case_word):
               result.append(word)
            
        return result


