class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        leftView = [1] * n
        rightView = [1] * n

        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                rightView[i] = rightView[i + 1] + 1

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                leftView[i] = leftView[i - 1] + 1

        result = 0
        for i in range(n):
            result += max(leftView[i], rightView[i])

        return result
