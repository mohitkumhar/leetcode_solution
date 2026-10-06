class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)

        result = [0] * n
        depth = 0

        for i in range(len(seq)):
            if seq[i] == "(":
                depth += 1
                result[i] = depth % 2

            else:
                result[i] = depth % 2
                depth -= 1

        return result
