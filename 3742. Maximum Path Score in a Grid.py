class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        memo = [[[-1 for _ in range(k + 1)] for _ in range(n + 1)] for _ in range(m + 1)]

        def solve(i, j, score, cost):
            if i >= m or j >= n:
                return float('-inf')

            val = grid[i][j]
            score += val

            if val > 0:
                cost += 1
            if cost > k:
                return float('-inf')
            
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            if memo[i][j][cost] != -1:
                return memo[i][j][cost]

            down = solve(i + 1, j, score, cost)
            right = solve(i, j + 1, score, cost)

            best_move = max(down, right)

            if best_move == float('-inf'):
                memo[i][j][cost] = best_move
            else:
                memo[i][j][cost] = best_move + grid[i][j]

            return best_move + grid[i][j]

        ans = solve(0,0,0,0) 

        return ans if ans != float('-inf') else -1
