class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        string = ' '.join(s.split())

        str_list = string.split()

        for i in reversed(str_list):
            ans = ans + i + ' '

        return ans.strip()
