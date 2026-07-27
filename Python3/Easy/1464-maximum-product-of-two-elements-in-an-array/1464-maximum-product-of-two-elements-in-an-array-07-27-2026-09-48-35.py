class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                result = max(result, ((nums[i]-1)*(nums[j]-1)))

        return result