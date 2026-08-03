class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()

        prev = -1
        count = 0

        target = (len(nums) // 2) + 1

        for num in nums:
            if num != prev:
                count = 1
            else:
                count += 1
            prev = num

            if count >= target:
                return num
