class Solution:
    def concatHex36(self, n: int) -> str:
        def convert_to_base(x, b):
            if x == 0:
                return "0"
            digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            result = ''

            while x > 0:
                result = digits[x % b] + result
                x //= b
            return result

        ans = ''
        ans += str(convert_to_base(n * n, 16))
        ans += str(convert_to_base(n * n * n, 36))

        return ans