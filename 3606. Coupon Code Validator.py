from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def check_code(code):
            if not code:
                return False
            for char in code:
                if not (char.isalnum() or char == '_'):
                    return False
            return True

        def check_business(string):
            all_business = ["electronics", "grocery", "pharmacy", "restaurant"]
            return string in all_business

        def check_isactive(cond):
            if cond:
                return True
            return False

        result = []
        for i in range(len(code)):
            if check_code(code[i]) and check_business(businessLine[i]) and check_isactive(isActive[i]):
                result.append((businessLine[i], code[i]))

        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        result.sort(key=lambda x: (order.index(x[0]), x[1]))

        return [c for _, c in result]
