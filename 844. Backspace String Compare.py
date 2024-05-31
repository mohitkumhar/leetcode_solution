class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def check(string):
            ans = []
            for i in range(len(string)):
                if string[i] == '#':
                    if ans:
                        ans.pop()
                else:
                    ans.append(string[i])

            return ans

        return check(s) == check(t)
