class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)

        result = []
        for i in range(n):
            if i % 2 == 0:
                result.append(even.pop(0))
            else:
                result.append(odd.pop(0))
        return result