class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        i = 0
        j = 0
        seen = set()
        n = len(nums)

        while j < n:
            if nums[j] in seen:
                return True

            seen.add(nums[j])

            if abs(j - i) < k:
                j += 1

            else:
                seen.remove(nums[i])
                i += 1
                j += 1

        return False
