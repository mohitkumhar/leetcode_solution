class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n = len(nums)

        minVal = min(nums)
        maxVal = max(nums)

        minIndex = nums.index(minVal)
        maxIndex = nums.index(maxVal)

        # delte both from left
        left = max(maxIndex, minIndex) + 1

        # delete both from right
        right = n - min(maxIndex, minIndex)

        # delete from both end
        mixed = 1 + min(minIndex, maxIndex) + n - max(minIndex, maxIndex)

        return min(left, right, mixed)
