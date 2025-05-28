class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for sentence in sentences:
            count = max(count, len(sentence.split()))

        return count
