class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(i, curr_comb):
            if len(curr_comb) == k:
                result.append(curr_comb[:])
                return

            if i == (n + 1):
                return

            for j in range(i, n + 1):
                curr_comb.append(j)

                backtrack(j + 1, curr_comb)

                curr_comb.pop()

        result = []
        backtrack(1, [])

        return result
