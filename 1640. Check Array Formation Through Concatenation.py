class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 1
            if count >= k:
                return True
        return False
