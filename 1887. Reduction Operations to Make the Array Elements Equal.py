class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        rank = {val: rank for rank, val in enumerate(sorted_nums)}

        return sum(rank[num] for num in nums)
