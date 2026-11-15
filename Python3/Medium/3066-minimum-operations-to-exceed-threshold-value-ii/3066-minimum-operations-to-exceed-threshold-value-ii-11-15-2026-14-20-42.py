class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        opn = 0

        while len(nums) > 1:
            small_1 = heapq.heappop(nums)
            small_2 = heapq.heappop(nums)

            if small_1 >= k:
                return opn

            newNum = small_1 * 2 + small_2
            heapq.heappush(nums, newNum)

            opn += 1

        return opn
