class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            freq = 0
            for j in range(i, n):
                if nums[j] == target:
                    freq += 1
                length = j - i + 1
                if 2 * freq > length:
                    count += 1
        return count
