class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(s='', start=0, end=0):
            if len(s) == 2 * n:
                result.append(''.join(s))
                return

            if start < n:
                backtrack(s + '(', start + 1, end)

            if end < start:
                backtrack(s + ')', start, end + 1)

        result = []

        backtrack()

        return result
