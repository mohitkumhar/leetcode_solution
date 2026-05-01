class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        ans = []

        for row in range(rows):
            for col in range(cols):
                dist = abs(rCenter - row) + abs(cCenter - col)
                ans.append([dist, row, col])

        ans.sort()
        result = [[row, col] for dist, row, col in ans]

        return result
