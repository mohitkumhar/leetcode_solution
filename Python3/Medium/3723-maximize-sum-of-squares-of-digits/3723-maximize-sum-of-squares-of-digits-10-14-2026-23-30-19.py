class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num * 9 < sum:
            return ""

        nines = sum // 9
        rem = sum % 9

        ans = ""
        for i in range(num):
            if nines:
                ans += "9"
                nines -= 1
            elif rem:
                ans += str(rem)
                rem = 0
            else:
                ans += "0"

        return ans
