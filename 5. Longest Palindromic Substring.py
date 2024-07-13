class Solution:
    def longestPalindrome(self, s: str) -> str:

        def check_from_middle(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            ans = s[left + 1: right]
            return ans

        ans = s[0]

        for i in range(len(s)):
            # For checking for odd length, when center is one

            palindrome1 = check_from_middle(i, i)
            if len(ans) < len(palindrome1):
                ans = palindrome1

            # For checking for even length, when center are two numbers
            palindrome2 = check_from_middle(i, i + 1)
            if len(ans) < len(palindrome2):
                ans = palindrome2

        return ans
