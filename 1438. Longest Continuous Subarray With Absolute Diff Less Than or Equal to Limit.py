import heapq

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        left = 0
        max_length = 0

        max_heap = []
        min_heap = []

        for right in range(len(nums)):

            heapq.heappush(min_heap, (nums[right], right))
            heapq.heappush(max_heap, (-nums[right], right))

            while max_heap and min_heap and abs(min_heap[0][0] - (-max_heap[0][0])) > limit:
                left = min(max_heap[0][1], min_heap[0][1]) + 1

                while min_heap and min_heap[0][1] < left:
                    heapq.heappop(min_heap)

                while max_heap and max_heap[0][1] < left:
                    heapq.heappop(max_heap)

            max_length = max(max_length, right - left + 1)

        return max_length
