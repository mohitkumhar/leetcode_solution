class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        def backtrack(i, children):
            nonlocal result

            if i >= len(cookies):
                result = min(result, max(children))
                return

            for j in range(k):
                children[j] += cookies[i]

                backtrack(i + 1, children)

                children[j] -= cookies[i]

                if children[j] == 0:
                    break

        result = float("inf")
        children = [0] * k

        backtrack(0, children)

        return result
