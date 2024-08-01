class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sum = 0

        for detail in details:
            if detail[-4:-2] > '60':
                sum += 1

        return sum
