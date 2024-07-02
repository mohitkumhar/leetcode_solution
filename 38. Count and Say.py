class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)

        result = ""

        i = 0
        while i < len(prev):
            ch = prev[i]
            count = 1

            while i < len(prev) - 1 and prev[i] == prev[i + 1]:
                count += 1
                i += 1
            result += str(count) + str(ch)
            i += 1

        return result
