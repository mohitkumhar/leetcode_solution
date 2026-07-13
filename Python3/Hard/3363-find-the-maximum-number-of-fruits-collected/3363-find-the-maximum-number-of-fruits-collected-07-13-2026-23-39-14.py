class Solution:
    def collect_child_1(self, fruits: List[List[int]]) -> int:
        count = 0
        for i in range(len(fruits)):
            count += fruits[i][i]
        return count

    def collect_child_2(
        self, i: int, j: int, moves: int, fruits: List[List[int]]
    , memo: List[List[int]]) -> int:
        n = len(fruits)
        if i >= n or j >= n or j < 0:
            return 0

        if moves > n - 1:
            return 0
        if moves == n - 1:
            return 0
        if i >= j:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        bottom_left = fruits[i][j] + self.collect_child_2(
            i + 1, j - 1, moves + 1, fruits, memo
        )
        bottom_down = fruits[i][j] + self.collect_child_2(i + 1, j, moves + 1, fruits, memo)
        bottom_right = fruits[i][j] + self.collect_child_2(
            i + 1, j + 1, moves + 1, fruits, memo
        )

        memo[i][j] =  max(bottom_left, bottom_down, bottom_right)
        return memo[i][j]

    def collect_child_3(
        self, i: int, j: int, moves: int, fruits: List[List[int]]
    , memo: List[List[int]]) -> int:
        n = len(fruits)
        if i < 0 or i >= n or j >= n:
            return 0

        if i <= j:
            return 0
        if moves >= n - 1:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        top_right = fruits[i][j] + self.collect_child_3(i - 1, j + 1, moves + 1, fruits, memo)
        right = fruits[i][j] + self.collect_child_3(i, j + 1, moves + 1, fruits, memo)
        bottom_right = fruits[i][j] + self.collect_child_3(
            i + 1, j + 1, moves + 1, fruits, memo
        )

        memo[i][j] = max(top_right, right, bottom_right)
        return memo[i][j]

    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        memo1 = [[-1 for _ in range(n)] for _ in range(n)]
        memo2 = [[-1 for _ in range(n)] for _ in range(n)]

        child_1_score = self.collect_child_1(fruits)
        child_2_score = self.collect_child_2(0, n - 1, 0, fruits, memo1)
        child_3_score = self.collect_child_3(n - 1, 0, 0, fruits, memo2)

        return child_1_score + child_2_score + child_3_score
