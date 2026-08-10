class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for k in range(n):
            if k > 0 and nums[k] == nums[k - 1]:  # use to avoid duplicates
                continue

            i = k + 1
            j = n - 1

            while i < j:

                currKey = nums[k] + nums[i] + nums[j]

                if currKey == 0:
                    result.append([nums[k], nums[i], nums[j]])

                    while i < j and nums[i] == nums[i + 1]:  # use to avoid duplicates
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:  # use to avoid duplicates
                        j -= 1

                    i += 1
                    j -= 1

                elif currKey > 0:
                    j -= 1

                else:
                    i += 1

        return result
