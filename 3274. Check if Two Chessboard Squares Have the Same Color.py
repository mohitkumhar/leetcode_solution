class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

        val1 = map[coordinate1[0]]
        val2 = int(coordinate1[1])
        num1 = map[coordinate2[0]]
        num2 = int(coordinate2[1])
        val = val1 + val2
        num = num1 + num2

        if val % 2== 0 and num % 2 == 0 or val % 2 == 1 and num % 2 == 1:
            return True
        return False
