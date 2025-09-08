class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            temp = word.split(separator)
            result.extend(temp)

        return [w for w in result if w]