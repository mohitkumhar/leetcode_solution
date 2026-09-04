class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        j = n - 1

        while j >= 0:
            if int(num[j]) % 2 == 1:
                return num[: j + 1]
            j -= 1

        return ""
