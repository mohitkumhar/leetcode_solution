class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefixSum = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixSum = [1]
        else:
            self.prefixSum.append(self.prefixSum[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.prefixSum)
        left = n - k
        right = n - 1

        if n <= k:
            return 0

        return self.prefixSum[-1] // self.prefixSum[n - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
