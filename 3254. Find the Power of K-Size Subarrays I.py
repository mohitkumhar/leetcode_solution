class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = []
        n = len(nums)
        i = 0
        j = 0
        bad_diff = 0

        while j < n:
            while queue and nums[queue[-1]] >= nums[j]:
                queue.pop()
            if queue:
                diff = nums[j] - nums[queue[-1]]
            queue.append(j)

            if j > 0 and nums[j] != (nums[j - 1] + 1):
                bad_diff += 1

            if (j - i + 1) == k:
                if len(queue) == k and bad_diff == 0:
                    ans.append(nums[queue[-1]])
                else:
                    ans.append(-1)

                if queue[0] == i:
                    queue.pop(0)
                
                if i + 1 < n and (nums[i] + 1) != nums[i + 1]:
                    bad_diff -= 1

                i += 1
            j += 1

        return ans
