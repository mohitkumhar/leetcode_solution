class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        prev = [1, 1]
        result = []
        for i in range(2, rowIndex + 1):
            curr = [1]

            j = 1
            while j < len(prev):
                curr.append(prev[j] + prev[j - 1])
                j += 1
            curr.append(1)

            result = curr
            prev = curr

        return result
