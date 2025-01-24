class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        add = 0

        for start in range(0, len(nums)):
            current_max = nums[start]
            current_min = nums[start]

            for end in range(start, len(nums)):

                current_max = max(current_max, nums[end])
                current_min = min(current_min, nums[end])

                add += (current_max - current_min)

        return add