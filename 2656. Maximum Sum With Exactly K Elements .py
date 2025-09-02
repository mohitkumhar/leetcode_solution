class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        val = max(nums)
        score = 0
        for _ in range(k):
            score += val
            val += 1
        return score