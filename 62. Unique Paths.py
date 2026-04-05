class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.unique = 0
        table = {}

        def solve(i, j):
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0
            if (i,j) in table:
                return table[(i, j)]

            self.unique = solve(i + 1, j) + solve(i, j+1)
            table[(i,j)] = self.unique
            return self.unique

        return solve(0,0)
