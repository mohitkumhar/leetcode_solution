class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        n = len(target)

        result = 0
        prev = 0
        curr = 0

        for i in range(n):
            curr = target[i]

            # check for the sign change
            if prev < 0 and curr > 0 or prev > 0 and curr < 0:
                result += abs(curr)

            elif curr > prev:
                result += abs(curr - prev)

            prev = curr

        return result
