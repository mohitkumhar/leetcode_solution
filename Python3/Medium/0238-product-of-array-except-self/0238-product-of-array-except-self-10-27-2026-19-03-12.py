class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        ans = []
        n = len(nums)

        for i in range(n):
            currProd = 1
            for j in range(n):
                if i != j:
                    currProd *= nums[j]
            ans.append(currProd)

        return ans
