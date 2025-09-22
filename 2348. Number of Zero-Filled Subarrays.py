class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        continus = 0
        count = 0
        for num in nums:
            if num == 0:
                continus += 1
                count += continus
            else:
                continus = 0

        return count