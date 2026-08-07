class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]

        result = [[1], [1, 1]]
        prev = [1, 1]
        
        for i in range(3, numRows + 1):
            currRow = [1]
            j = 1

            while j < len(prev):
                currRow.append(prev[j - 1] + prev[j])
                j += 1
            currRow.append(1)
            result.append(currRow)
            prev = currRow
        return result