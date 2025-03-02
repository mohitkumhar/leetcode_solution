class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        map = {}
        
        for num in nums1:
            if num[0] in map:
                map[num[0]] += num[1]
            else:
                map[num[0]] = num[1]
        
        for num in nums2:
            if num[0] in map:
                map[num[0]] += num[1]
            else:
                map[num[0]] = num[1]
        
        keys = list(map.keys())
        values = list(map.values())

        result = []
        for i in range(len(keys)):
            result.append([keys[i], values[i]])

        result.sort(key=lambda x: x[0])
        return result