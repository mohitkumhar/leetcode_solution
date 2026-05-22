class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for num in nums:
            count += str(num).count(str(digit))

        return count
