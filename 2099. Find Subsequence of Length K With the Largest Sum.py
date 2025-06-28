class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        index_nums = [(num, i) for i, num in enumerate(nums)]

        top_k = sorted(index_nums, key=lambda x: x[0], reverse=True)[:k]

        top_k.sort(key=lambda x:x[1])

        return [val for val, _ in top_k]
