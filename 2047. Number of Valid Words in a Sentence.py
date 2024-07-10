class Solution:
    def countValidWords(self, sentence: str) -> int:

        def helper(token):
            # check lower letter and symbols
            valid_chars = set('abcdefghijklmnopqrstuvwxyz-,.!')
            if any(word not in valid_chars for word in token):
                return False

            # check hyphens
            if '-' in token:
                pairs = token.split('-')
                if len(pairs) != 2 or not pairs[0].islower() or not pairs[1].islower():
                    return False

            # check punctuation
            punctuation = set('.,!')
            if any(char in punctuation for char in token[:-1]):
                return False
            return True

        tokens = sentence.split()

        valid_word_count = 0

        for token in tokens:
            if helper(token):
                valid_word_count += 1

        return valid_word_count
