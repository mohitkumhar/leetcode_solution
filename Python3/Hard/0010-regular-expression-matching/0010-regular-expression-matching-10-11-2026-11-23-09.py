class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def solve(word, pattern):
            if len(pattern) == 0:
                return len(word) == 0

            firstCharMatched = False

            if len(word) > 0 and (word[0] == pattern[0] or pattern[0] == "."):
                firstCharMatched = True

            # check for *

            if len(pattern) > 1 and pattern[1] == "*":
                notTake = solve(word, pattern[2:])
                take = firstCharMatched and solve(word[1:], pattern)

                return notTake or take

            # check for normal chars
            return firstCharMatched and solve(word[1:], pattern[1:])

        return solve(s, p)
