class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False

        i = 0

        while i+1 < len(nums) and nums[i] < nums[i + 1]:
            i += 1

        if i == 0:
            return False
        j = i

        while j+1 < len(nums) and nums[j] > nums[j + 1]:
            j += 1

        if j == i:
            return False
        k = j

        while k+1 < len(nums) and nums[k] < nums[k + 1]:
            k += 1

        if k == j:
            return False
        j = i

        return k == len(nums) - 1
