class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []

        for i in range(0, len(s), k):
            word = s[i: i + k]
            result.append(word)

        while len(result[-1]) < k:
            result[-1] += fill

        return result
