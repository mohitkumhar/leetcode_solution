class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        def freq_check(word):
            check = {}
            for char in word:
                if char in check:
                    check[char] += 1
                else:
                    check[char] = 1
            return check

        common_freq = freq_check(words[0])

        for word in words[1:]:
            duplicate_freq = freq_check(word)

            temp = {}

            for char in common_freq:
                if char in duplicate_freq:
                    temp[char] = min(common_freq[char], duplicate_freq[char])

            common_freq = temp

        result = []

        for char in common_freq:
            result.extend([char] * common_freq[char])

        return result
