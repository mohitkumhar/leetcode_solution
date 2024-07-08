class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        result = [i for i in range(1, n + 1)]
        index = 0

        while len(result) > 1:
            size = len(result)
            index = (index + k - 1) % size
            result.pop(index)

        return result[0]
