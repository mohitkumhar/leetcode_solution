class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        dictionary.sort(key=len)

        words = sentence.split()

        def change(word):
            for root in dictionary:
                if word.startswith(root):
                    return root

            return word

        ans = [change(word) for word in words]

        return ' '.join(ans)
