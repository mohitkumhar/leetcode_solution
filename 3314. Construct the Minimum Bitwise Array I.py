class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            is_found = False
            for i in range(num):
                if i | (i + 1) == num:
                    ans.append(i)
                    is_found = True
                    break

            if not is_found:
                ans.append(-1)

        return ans
