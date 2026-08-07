class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        seen = set(words)
        result = []

        def check(word):
            if word in seen:
                return True
            if word in memo:
                return memo[word]

            for i in range(len(word) - 1):
                if check(word[: i + 1]) and check(word[i + 1 :]):
                    memo[word] = True
                    return True

            memo[word] = False
            return False

        for word in words:
            memo = {}
            seen.remove(word)
            for i in range(len(word) - 1):
                prefix = word[: i + 1]
                suffix = word[i + 1 :]

                if check(prefix) and check(suffix):
                    result.append(word)
                    break
            seen.add(word)

        return result
