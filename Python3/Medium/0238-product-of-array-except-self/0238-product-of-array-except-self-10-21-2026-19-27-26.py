class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = []

        for i in range(n):
            currProd = 1

            for j in range(n):
                if i == j:
                    continue
                currProd *= nums[j]
            
            result.append(currProd)
        
        return result

