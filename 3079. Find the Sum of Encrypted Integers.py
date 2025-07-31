class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def replace(val):
            digits = []
            for num in str(val):
                digits.append(num)
            max_digit = max(digits)
            for i in range(len(digits)):
                digits[i] = max_digit

            return int(''.join(digits))

        ans = 0
        for num in nums:
            ans += replace(num)
        return ans
