class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if min(nums) < num and num < max(nums) :
                count += 1
        return count
