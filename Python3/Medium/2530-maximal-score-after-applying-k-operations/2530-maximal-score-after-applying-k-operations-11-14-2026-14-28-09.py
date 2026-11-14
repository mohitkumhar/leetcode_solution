class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:

        nums = [-num for num in nums]
        heapq.heapify(nums)

        ans = 0

        for _ in range(k):

            currNum = -heapq.heappop(nums)
            ans += currNum

            currNumCeil = (currNum + 2) // 3

            heapq.heappush(nums, -currNumCeil)

        return ans
