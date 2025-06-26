class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            num = str(i)
            if len(num) % 2 == 1:
                continue
            if sum(int(digit) for digit in num[:len(num) // 2]) == sum(int(digit) for digit in num[len(num) // 2:]):
                count += 1

        return count
