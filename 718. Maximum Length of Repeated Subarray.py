class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        check_list = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        max_length = 0

        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):

                if nums1[i - 1] == nums2[j - 1]:
                    check_list[i][j] = check_list[i - 1][j - 1] + 1
                    max_length = max(max_length, check_list[i][j])

        return max_length