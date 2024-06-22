class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        odd_count = 0
        result = 0
        map_count = {0: 1}

        for i in nums:
            if i % 2 != 0:
                odd_count += 1

            if odd_count in map_count:
                map_count[odd_count] += 1
            else:
                map_count[odd_count] = 1

            if odd_count - k in map_count:
                result += map_count[odd_count - k]

        return result
