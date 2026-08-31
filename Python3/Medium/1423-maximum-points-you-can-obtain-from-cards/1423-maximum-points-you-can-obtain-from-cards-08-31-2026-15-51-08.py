class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        total = sum(cardPoints)
        if k == n:
            return total

        windowSize = n - k

        currSum = 0
        i = 0
        ans = float("inf")

        for j in range(n):

            currSum += cardPoints[j]

            if j - i + 1 == windowSize:
                ans = min(ans, currSum)

                currSum -= cardPoints[i]
                i += 1

        print(total - ans)
        return total - ans
