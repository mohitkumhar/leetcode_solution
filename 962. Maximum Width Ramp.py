class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_width = 0
        vp = [(nums[i], i) for i in range(len(nums))]
        vp.sort()
        min_index = vp[0][1]

        for i in range(1, len(nums)):
            current_index = vp[i][1]
            max_width = max(max_width, current_index - min_index)
            min_index = min(min_index, current_index)
        
        return max_width
