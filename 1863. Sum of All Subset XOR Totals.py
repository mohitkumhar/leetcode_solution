class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sub_array = []

        def backtrack(index, current):
            if index == len(nums):
                sub_array.append(current)
                return 
            
            backtrack(index + 1, current)
            backtrack(index + 1, current + [nums[index]])
    
        backtrack(0, [])
        total = 0

        for arr in sub_array:
            xor_val = 0
            for num in arr:
                xor_val ^= num
            total += xor_val
    
        return total
