class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def backtrack(i, used_comb):
            nonlocal count

            if i >= len(s):
                count = max(count, len(used_comb))
                return

            for j in range(i, len(s)):
                if s[i : j + 1] in used_comb:
                    continue
                used_comb.add(s[i : j + 1])
                backtrack(j + 1, used_comb)
                used_comb.remove(s[i : j + 1])

        used_comb = set()
        count = 0

        backtrack(0, used_comb)

        return count
