class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        words.sort()

        for word in words:
            if any(word in item for item in words if word != item):
                result.append(word)

        return result
