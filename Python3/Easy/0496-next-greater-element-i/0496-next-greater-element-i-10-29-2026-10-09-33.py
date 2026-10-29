class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        result = []
        for val in nums1:
            j = 0
            while nums2[j] != val:
                j += 1

            maxVal = -1
            for i in range(j, len(nums2)):
                if nums2[i] > val:
                    maxVal = nums2[i]
                    break
            result.append(maxVal)

        return result
