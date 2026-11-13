class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        freq = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

        a = freq.get(coordinates[0])
        b = int(coordinates[1])

        if (a + b) % 2 == 0:
            return False
        return True
