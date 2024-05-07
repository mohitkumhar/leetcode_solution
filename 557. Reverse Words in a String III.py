class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []

        s_list = [s.split(" ")]

        for i in s_list:
            ans.append(i[::-1])

        result = ""
        for i in ans:
            for j in i:
                result = j[::-1] + " " + result

        return result.strip()
        