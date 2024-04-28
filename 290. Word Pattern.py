class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        map_word = {}
        map_char = {}

        word_list = s.split(" ")

        if ( len(pattern) != len(word_list) ):
            return False

        for word, char in zip(word_list, pattern):
            if char not in map_char:

                if word in map_word:
                    return False

                else:
                    map_word[word] = char
                    map_char[char] = word
                
            else:
                if map_char[char] != word:
                    return False

        return True






