class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for i in count:
            if count[i] == n:
                return i
