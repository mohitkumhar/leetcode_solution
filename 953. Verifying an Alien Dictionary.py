class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_index = {c: i for i, c in enumerate(order)}

        def compare(word1, word2):
            for w1, w2 in zip(word1, word2):
                if order_index[w1] < order_index[w2]:
                    return True

                if order_index[w1] > order_index[w2]:
                    return False

            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not compare(words[i], words[i + 1]):
                return False

        return True
