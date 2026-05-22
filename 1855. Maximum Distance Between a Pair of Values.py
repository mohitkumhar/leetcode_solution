class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        max_distance = 0

        for i in range(n1):
            start = i
            end = n2 - 1

            while start <= end:
                mid = (start + end) // 2

                if nums2[mid] >= nums1[i]:
                    max_distance = max(max_distance, mid - i)
                    start = mid + 1

                else:
                    end = mid - 1

        return max_distance
