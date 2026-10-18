class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False
