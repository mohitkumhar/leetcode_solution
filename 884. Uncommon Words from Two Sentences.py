class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words_s1 = s1.split()
        words_s2 = s2.split()

        word_count = {}

        for word in words_s1 + words_s2:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

        uncommon = [word for word in word_count if word_count[word] == 1]

        return uncommon
