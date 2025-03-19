class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        def turn(i):
            if nums[i] == 0:
                nums[i] = 1
            else:
                nums[i] = 0


        count = 0

        for i in range(len(nums)):
            if i < len(nums) - 2 and nums[i] == 0:
                turn(i)
                turn(i+1)
                turn(i+2)
                count += 1
        
        if (list(set(nums))[0]) == 1:
            return count
        return -1
