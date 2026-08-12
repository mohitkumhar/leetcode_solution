class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        map = {}
        j = 0
        count = 0

        for i in range(n):

            while j < n:
                value = nums[j]
                map[value] = map.get(value, 0) + 1

                j += 1

                if map[value] > k:
                    j -= 1
                    map[value] -= 1
                    break

            count = max(count, j - i)

            map[nums[i]] -= 1

        return count
