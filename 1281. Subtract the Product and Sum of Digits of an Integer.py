class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)

        product = 1
        sum = 0

        for i in n_str:
            product *= int(i) 
            sum += int(i)

        return product - sum
