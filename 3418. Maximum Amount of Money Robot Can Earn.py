class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        m = len(coins)
        n = len(coins[0])
        table = [[[None] * 3 for _ in range(n)] for _ in range(m)] 

        def solve(coin, i, j, neu):

            if i >= m or j >= n:
                return float('-inf')

            if i == m - 1 and j == n - 1:
                if coins[i][j] < 0 and neu > 0:
                    return 0

                return coins[i][j]
            
            if table[i][j][neu] != None:
                return table[i][j][neu]


            
            # taking the coin from curr cell
            take = coin[i][j] + max(solve(coin, i+1 , j, neu), solve(coin, i, j+1, neu))

            # skiping coin if possible
            skip = float('-inf')

            if coins[i][j] < 0 and neu > 0:
                skip_right = solve(coin, i, j+1, neu-1)
                skip_down = solve(coin, i+1, j, neu-1)
            
                skip = max(skip_right, skip_down)
            
            table[i][j][neu] = max(take, skip)
            return max(take, skip)

        return solve(coins, 0, 0, 2)
