class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def get_ops(target):
            arr = nums[:]
            count = 0

            for i in range(len(arr) -1):
                if arr[i] != target:
                    arr[i] *= -1
                    arr[i + 1] *= -1
                    count += 1

            return count if arr[-1] == target else float('inf')

        min_ops = min(get_ops(1), get_ops(-1))

        return min_ops <= k