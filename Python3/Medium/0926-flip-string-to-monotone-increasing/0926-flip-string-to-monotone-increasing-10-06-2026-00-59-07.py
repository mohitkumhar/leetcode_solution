class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        countOne = 0
        flip = 0

        for char in s:
            if char == "1":
                countOne += 1

            else:
                flip += 1
                flip = min(flip, countOne)

        return flip
