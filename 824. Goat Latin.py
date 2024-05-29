class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """

        vowel = set('aeiouAEIOU')
        words = sentence.split()

        goat_ans = []

        for i, word in enumerate(words):
            if word[0] in vowel:
                goat_word = word + 'ma'

            else:
                goat_word = word[1:] + word[0] + 'ma'

            goat_word = goat_word + 'a' * (i + 1)

            goat_ans.append(goat_word)

        return ' '.join(goat_ans)
