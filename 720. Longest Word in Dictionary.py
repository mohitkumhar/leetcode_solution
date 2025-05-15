class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words_check = set()
        maximum = ''

        for word in words:
            if len(word) == 1 or word[:-1] in words_check:
                words_check.add(word)

                if len(word) > len(maximum):
                    maximum = word

        return maximum
