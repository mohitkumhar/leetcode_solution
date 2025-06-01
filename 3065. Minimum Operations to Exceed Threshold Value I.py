class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for num in nums:
            if num < k:
                count += 1
        return count
