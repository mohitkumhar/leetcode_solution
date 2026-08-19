class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        def check(num, row):
            return num not in count.get(row, {})

        count = {}

        for row, seat in reservedSeats:
            if row not in count:
                count[row] = set()
            count[row].add(seat)

        result = (n - len(count)) * 2

        for i in count:
            group1 = check(2, i) and check(3, i) and check(4, i) and check(5, i)
            group2 = check(4, i) and check(5, i) and check(6, i) and check(7, i)
            group3 = check(6, i) and check(7, i) and check(8, i) and check(9, i)

            if group1 and group3:
                result += 2
            elif group1 or group2 or group3:
                result += 1

        return result
