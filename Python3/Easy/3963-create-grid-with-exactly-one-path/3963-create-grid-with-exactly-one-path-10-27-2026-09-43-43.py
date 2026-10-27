class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        result = []

        for i in range(m):
            currStr = ""

            for j in range(n):
                if i == 0:
                    currStr += "."
                elif j == (n - 1):
                    currStr += "."
                else:
                    currStr += "#"
            result.append(currStr)

        return result
