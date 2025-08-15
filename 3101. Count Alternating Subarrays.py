class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        length = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                length += 1
            else:
                length = 1
            count += length
        return count