class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def digit_sum(nums):
            sum = 0
            while nums != 0:
                sum += nums % 10
                nums //= 10
            return sum

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        counter = {}
        count = 0

        for i in range(len(nums)):
            counter[nums[i]] = i

        for i in range(len(nums)):
            if nums[i] != arr[i]:
                j = counter[arr[i]]

                nums[i], nums[j] = nums[j], nums[i]

                counter[nums[i]] = i
                counter[nums[j]] = j

                count += 1

        return count
