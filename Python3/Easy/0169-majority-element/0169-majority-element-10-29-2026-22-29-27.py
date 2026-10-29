class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        maxElement = (len(nums) // 2) + 1
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

            if freq[num] >= maxElement:
                return num
        return -1
