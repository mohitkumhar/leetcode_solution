class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        count = 0
        prev = None
        ans = []
        for num in nums:
            if num == prev:
                count += 1
            else:
                count = 1

            if count <= k:
                ans.append(num)


            prev = num

        return ans
