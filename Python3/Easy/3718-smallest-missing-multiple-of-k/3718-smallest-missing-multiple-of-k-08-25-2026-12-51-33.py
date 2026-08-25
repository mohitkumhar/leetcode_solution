class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        for i in range(1, max(nums) + k + 1):
            if i not in nums and i % k == 0:
                return i
