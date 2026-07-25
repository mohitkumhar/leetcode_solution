class Solution:
    def maxProduct(self, n: int) -> int:
        result = []
        for num in str(n):
            result.append(int(num))
        result.sort(reverse=True)

        return result[0] * result[1]
