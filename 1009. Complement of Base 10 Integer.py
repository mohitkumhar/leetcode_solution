class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """

        sum_bin = bin(n)[2:]
        print(sum_bin)

        ans = ''.join('1' if i == '0' else '0' for i in sum_bin)

        return int(ans, 2)


        