class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 1
        if not nums:
            return 0

        check = set(nums)

        for num in check:
            if num - 1 in check:
                continue

            else:
                currDiff = 1
                temp = num

                while temp + 1 in check:
                    temp += 1
                    currDiff += 1

                ans = max(ans, currDiff)

        return ans
