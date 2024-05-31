class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_dollor = 0
        ten_dollor = 0

        for bill in bills:
            if bill == 5:
                five_dollor += 1

            elif bill == 10:
                if five_dollor == 0:
                    return False

                five_dollor -= 1
                ten_dollor += 1

            elif bill == 20:
                if ten_dollor > 0 and five_dollor > 0:
                    ten_dollor -= 1
                    five_dollor -= 1

                elif five_dollor >= 3:
                    five_dollor -= 3
                else:
                    return False

        return True
