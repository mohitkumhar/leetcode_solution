class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)
        found_one = False
        is_one = 0
        ans = 0

        for i in range(len(binary)):
            if binary[i] == "1" and not found_one:
                is_one = i
                found_one = True

            elif binary[i] == "1" and found_one:
                ans = max(ans, abs(is_one - i))
                is_one = i

        return ans
