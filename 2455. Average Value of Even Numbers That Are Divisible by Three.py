class Solution:
    def averageValue(self, nums: List[int]) -> int:
        value = []

        for num in nums:
            if num % 2 == 0:
                if num % 3 == 0:
                    value.append(num)
        
        if len(value) != 0:
            return sum(value) // len(value)

        else:
            return 0