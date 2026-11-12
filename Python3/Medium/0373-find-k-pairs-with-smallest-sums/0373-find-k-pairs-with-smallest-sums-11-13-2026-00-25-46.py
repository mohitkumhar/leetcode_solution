class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        m = len(nums1)
        n = len(nums2)

        heap = []

        for i in range(m):
            for j in range(n):
                currSum = nums1[i] + nums2[j]

                if len(heap) < k:
                    # ab to daalna hi h
                    heapq.heappush(heap, (-currSum, i, j))

                elif -heap[0][0] > currSum:
                    # currSum daal skte h
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-currSum, i, j))

                else:
                    # currSum bada is heap ke max element se... to break kr dnge... aage bhi sb bade honge
                    break

        ans = []
        for currSum, i, j in heap:
            ans.append([nums1[i], nums2[j]])

        return ans
