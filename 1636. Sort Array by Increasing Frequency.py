class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        def sort_key(num):
            return [count[num], -num]

        nums.sort(key=sort_key)

        return nums