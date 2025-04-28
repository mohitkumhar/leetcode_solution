class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        ans = []
        texts = (text.lower()).split(' ')
        texts.sort(key = lambda x: len(x))
        texts[0] = texts[0].capitalize()

        return ' '.join(texts)
        