class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breakPoint = -1
        n = len(nums)

        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                breakPoint = i - 1
                break

        if breakPoint == -1:
            nums.reverse()
            return

        for j in range(n - 1, breakPoint - 1, -1):
            if nums[j] > nums[breakPoint]:
                nums[j], nums[breakPoint] = nums[breakPoint], nums[j]
                break
        left = breakPoint + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
