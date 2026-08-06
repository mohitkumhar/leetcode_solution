class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []

        m = len(nums1)
        n = len(nums2)

        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1

            else:
                result.append(nums2[j])
                j += 1

        while i < m:
            result.append(nums1[i])
            i += 1

        while j < n:
            result.append(nums2[j])
            j += 1

        n = len(result)
        if n % 2 == 1:
            return result[n // 2]

        return (result[(n // 2) - 1] + result[n // 2]) / 2
