class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        def find_even(nums):
            for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    val = nums[i]
                    nums.pop(i)
                    return val

        def find_odd(nums):
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    val = nums[i]
                    nums.pop(i)
                    return val

        result = []

        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(find_even(nums))

            else:
                result.append(find_odd(nums))

        return result
