class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = sorted(str(num))

        num1 = int(num[0] + num[2])
        num2 = int(num[1] + num[3])

        return num1 + num2
