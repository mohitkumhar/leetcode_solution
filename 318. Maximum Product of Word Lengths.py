class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def words_match(word1, word2):
            word2 = set(word2)
            for w in word1:
                if w in word2:
                    return False
            return True

        max_len = 0

        for i in range(len(wodfrds)):
            for j in range(i + 1, len(words)):
                if words_match(words[i], words[j]):
                    max_len = max(max_len, len(words[i]) * len(words[j]))

        return max_len
