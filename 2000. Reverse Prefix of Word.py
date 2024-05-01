class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        
        index = word.index(ch)
        word_to_reverse = word[:index + 1]
        reverse_word = word_to_reverse[::-1]
        remaining_word = word[index+1:]
        
        return reverse_word + remaining_word