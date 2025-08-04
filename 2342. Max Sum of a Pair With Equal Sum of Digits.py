class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_count(value):
            return sum(int(i) for i in str(value))

        count = {}
        max_sum = -1

        for num in nums:
            digits = digit_count(num)

            if digits in count:
                max_sum = max(max_sum, count[digits] + num)
                count[digits] = max(count[digits], num)

            else:
                count[digits] = num
        return max_sum
