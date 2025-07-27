class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [True] * len(nums)
        nums = list(enumerate(nums))
        nums = sorted(nums, key = lambda x: x[1])
        score = 0

        for ind, val in nums:
            if marked[ind]:
                score += val
                marked[ind] = False

                if ind - 1 >= 0:
                    marked[ind - 1] = False
                if ind + 1 < len(nums):
                    marked[ind + 1] = False
        return score
