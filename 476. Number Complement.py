class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum_num = bin(num)[2:]
        ans = ''.join('0' if i == '1' else '1' for i in sum_num)
        return int(ans, 2)
        