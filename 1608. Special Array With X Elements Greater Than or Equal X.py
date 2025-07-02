class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            count = sum(num >= i for num in nums)

            if count == i:
                return i
        return -1
