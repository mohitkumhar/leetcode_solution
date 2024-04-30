class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        xor_value = x ^ y

        count = 0

        while(xor_value != 0):
            count += 1
            xor_value = xor_value & (xor_value - 1)
        
        return count
        