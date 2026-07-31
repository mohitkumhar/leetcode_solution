class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        sign = 1
        num = str(x)

        sign = -1 if num[0] == "-" else 1
        if sign == -1:
            num = num[1:]

        num = int(num[::-1])

        num *= sign

        if num >= INT_MAX or num <= INT_MIN:
            return 0
        return num
