class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))

        while k:
            arr.sort()

            val, idx = arr[0]
            arr[0] = (val * multiplier, idx)

            k -= 1

        ans = [0] * len(nums)

        for val, key in arr:
            ans[key] = val

        return ans
