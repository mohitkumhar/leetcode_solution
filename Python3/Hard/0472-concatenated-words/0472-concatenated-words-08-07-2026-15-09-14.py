class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        elements = set(words)

        def check(word):
            if word in elements:
                return True
            if word in memo:
                return memo[word]

            for i in range(len(word) - 1):
                prefix = word[: i + 1]
                suffix = word[i + 1 :]

                if check(prefix) and check(suffix):
                    memo[word] = True
                    return True

            memo[word] = False
            return False

        n = len(words)
        result = []

        for word in words:
            memo = {}

            elements.remove(word)
            for i in range(len(word) - 1):

                prefix = word[: i + 1]
                suffix = word[i + 1 :]

                if check(prefix) and check(suffix):
                    result.append(word)
                    break
            elements.add(word)

        return result
