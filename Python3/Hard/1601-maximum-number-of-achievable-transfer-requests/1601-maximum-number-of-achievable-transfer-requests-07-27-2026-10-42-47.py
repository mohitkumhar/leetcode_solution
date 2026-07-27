class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        def backtrack(i, curr_count, resultant):
            nonlocal result
            if i == len(requests):
                if all(x == 0 for x in resultant):
                    result = max(result, curr_count)
                return

            # take
            resultant[requests[i][0]] -= 1
            resultant[requests[i][1]] += 1

            backtrack(i + 1, curr_count + 1, resultant)

            resultant[requests[i][0]] += 1
            resultant[requests[i][1]] -= 1

            # skip
            backtrack(i + 1, curr_count, resultant)

        result = 0
        resultant = [0] * n

        backtrack(0, 0, resultant)

        return result
