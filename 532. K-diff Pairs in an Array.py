class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    pair = tuple(sorted((nums[i], nums[j])))
                    seen.add(pair)
        return len(seen)
