class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(num):
            counter = 0
            while num != 1:
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
                counter += 1
            return counter

        result = {}
        for num in range(lo, hi + 1):
            result[num]= power(num)

        return sorted(result.items(), key=lambda x: x[1])[k - 1][0]
