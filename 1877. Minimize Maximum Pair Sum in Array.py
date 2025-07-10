class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = []

        for i in range(len(nums) // 2):
            result.append(nums.pop() + nums.pop(0))

        return max(result)
