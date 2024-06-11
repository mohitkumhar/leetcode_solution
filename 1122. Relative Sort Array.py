class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        count = {}
        for num in arr1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        result = []
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]

        remaining = []
        for num in arr1:
            if num in count:
                remaining.extend([num] * count[num])
                del count[num]

        return result+sorted(remaining)
