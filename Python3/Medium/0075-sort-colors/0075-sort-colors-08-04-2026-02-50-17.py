class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1

        k = 0
        while zeros != 0:
            nums[k] = 0
            k += 1
            zeros -= 1

        while ones != 0:
            nums[k] = 1
            k += 1
            ones -= 1

        while twos != 0:
            nums[k] = 2
            k += 1
            twos -= 1
