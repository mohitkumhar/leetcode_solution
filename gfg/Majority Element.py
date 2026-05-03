class Solution:
    def majorityElement(self, arr):
        counter = {}

        for char in arr:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1


        limit = len(arr) // 2

        for key, value in counter.items():
            if value > limit:
                return key
        return -1
