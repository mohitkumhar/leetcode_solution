class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        for nums in range(n, 101):
            curr = 1
            for num in str(nums):
                curr *= int(num)

            if curr == 0 or curr % t == 0:
                return nums
