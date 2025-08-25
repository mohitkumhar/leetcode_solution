class Solution:
    def maxProduct(self, n: int) -> int:
        nums = str(n)
        res = []
        for num in nums:
            res.append(int(num))
        res.sort(reverse=True)
        return res[0] * res[1]
