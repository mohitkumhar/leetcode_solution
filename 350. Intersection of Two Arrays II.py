class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        result = []

        for i in range(len(nums1)):
            if nums1[i] in map:
                map[nums1[i]] += 1

            else:
                map[nums1[i]] = 1

        for j in range(len(nums2)):
            if nums2[j] in map and map[nums2[j]] >= 1:
                result.append(nums2[j])
                map[nums2[j]] -= 1

        return result
