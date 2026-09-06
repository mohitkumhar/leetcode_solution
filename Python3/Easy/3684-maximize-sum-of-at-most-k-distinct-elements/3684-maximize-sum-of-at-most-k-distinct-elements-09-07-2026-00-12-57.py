class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = list(set(nums))
        nums.sort(reverse=True)

        return nums[:k]
