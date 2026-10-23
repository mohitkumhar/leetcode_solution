class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        maxElement = max(nums)

        n = len(nums)

        currMaxEle = 0

        i = 0
        j = 0

        while j < n:
            if nums[j] == maxElement:
                currMaxEle += 1

            while i <= j and currMaxEle >= k:
                ans += n - j

                if nums[i] == maxElement:
                    currMaxEle -= 1
                i += 1
            j += 1

        return ans
