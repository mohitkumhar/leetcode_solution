class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)

        value_percentage = n * (25 / 100)

        count = {}

        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for i in count:
            if count[i] > value_percentage:
                return i

        return -1
