class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_s = s.strip()

        if new_s == "":
            return 0

        ans = 1

        for i in range(1, len(new_s)):
            if new_s[i] == " " and new_s[i - 1] != " ":
                ans += 1

        return ans
