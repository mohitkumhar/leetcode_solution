import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if not c:
            return True

        for a in range(int(math.sqrt(c))+1):

            b2 = c - a * a

            if b2 >= 0:
                b = int(math.sqrt(b2))
                if b * b == b2:
                    return True

        return False
