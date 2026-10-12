class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        cnt = [sum(x >> b & 1 for x in nums) for b in range(30)]  # coins in each bit column, never changes
        total = 0
        for i in range(k):  # build row i of the stacked picture
            row = sum(1 << b for b in range(30) if cnt[b] > i)  # a coin from every column with more than i coins
            total += row * row
        return total % (10**9 + 7)