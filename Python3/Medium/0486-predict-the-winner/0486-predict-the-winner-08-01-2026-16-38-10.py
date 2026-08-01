class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def solve(i, j):
            if i > j:
                return 0

            if i == j:
                return nums[i]

            take_i = nums[i] + min(solve(i + 2, j), solve(i + 1, j - 1))

            take_j = nums[j] + min(solve(i, j - 2), solve(i + 1, j - 1))

            return max(take_i, take_j)

        player1_score = solve(0, len(nums) - 1)
        player2_score = sum(nums) - player1_score

        return player1_score >= player2_score
