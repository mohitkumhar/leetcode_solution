class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        def solve(i, diff):
            if i == n:
                if diff == 0:
                    return 0
                return float("-inf")

            if memo[i][diff] != -1:
                return memo[i][diff]

            # add in l1
            add_in_l1 = rods[i] + solve(i + 1, diff + rods[i])

            # add in l2
            add_in_l2 = rods[i] + solve(i + 1, diff - rods[i])

            # add nothing
            add_nothing = solve(i + 1, diff)

            memo[i][diff] = max(add_in_l1, add_in_l2, add_nothing)
            return memo[i][diff]

        n = len(rods)
        total = sum(rods)

        memo = [[-1 for _ in range(total + 1)] for _ in range(n + 1)]

        return (
            solve(0, 0) // 2
        )  # it returns the length of both of the rods, and we want to return the length of the one rod, so we divide it with 2
