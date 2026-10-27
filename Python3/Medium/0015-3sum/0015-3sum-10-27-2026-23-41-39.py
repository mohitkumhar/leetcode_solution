class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        n = len(nums)
        result = []

        for k in range(n):
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i = k + 1
            j = n - 1

            while i < j:
                currVal = nums[i] + nums[j] + nums[k]

                if currVal == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif currVal > 0:
                    j -= 1

                else:
                    i += 1

        return result
