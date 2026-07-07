class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        sum = 0
        for num in str(n):
            if num != "0":
                x += num
                sum += int(num)

        return int(x) * sum if x else 0
