class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        # child 1
        def count_child1():
            count = 0
            for i in range(n):
                count += fruits[i][i]
            return count

        # child2
        memo2 = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        def count_child2(i, j):
            if i >= n or j >= n or j < 0:
                return 0
            if memo2[i][j] != -1:
                return memo2[i][j]

            if i == j or i > j:
                return 0

            move1 = fruits[i][j] + count_child2(i + 1, j - 1)
            move2 = fruits[i][j] + count_child2(i + 1, j)
            move3 = fruits[i][j] + count_child2(i + 1, j + 1)

            ans = max(move1, move2, move3)
            memo2[i][j] = ans

            return ans

        # child3
        memo3 = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        def count_child3(i, j):
            if i >= n or j >= n or j < 0 or i < 0:
                return 0
            if memo3[i][j] != -1:
                return memo3[i][j]

            if i == j or i < j:
                return 0

            move1 = fruits[i][j] + count_child3(i - 1, j + 1)
            move2 = fruits[i][j] + count_child3(i, j + 1)
            move3 = fruits[i][j] + count_child3(i + 1, j + 1)

            memo3[i][j] = max(move1, move2, move3)
            return memo3[i][j]

        child1 = count_child1()
        child2 = count_child2(0, n - 1)
        child3 = count_child3(n - 1, 0)

        return child1 + child2 + child3
