class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        left = 0
        max_length = 0
        bitmask = 0

        for right in range(len(nums)):

            while (bitmask & nums[right]) != 0:
                bitmask = bitmask ^ nums[left]
                left += 1
            
            bitmask = bitmask | nums[right]

            max_length = max(max_length, right - left + 1)

        return max_length
        