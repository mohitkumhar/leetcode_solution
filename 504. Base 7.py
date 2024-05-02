class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
            
        ans = ""

        is_negative = num < 0

        num = abs(num)

        while num > 0:
            rem = num % 7
            num = num / 7

            ans = str(rem) + ans
        
        if is_negative:
            ans = "-" + ans
        
        return ans