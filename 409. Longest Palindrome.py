class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = {}

        for i in s:
            if i not in ans:
                ans[i] = 1

            else:
                ans[i] += 1

        sum = 0
        odd = False

        for key, value in ans.items():
            if value % 2 != 0:
                value -= 1
                odd = True
            sum += value

        if odd:
            sum += 1

        return sum
