class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed = 0

        while x > 0:
            digit = x % 10
            reversed = (10 * reversed) + digit
            x = x // 10

        return original == reversed
