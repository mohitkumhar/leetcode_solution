class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dist_ele = set(nums)
        total = len(dist_ele)
        count = 0

        for left in range(len(nums)):
            found = set()

            for right in range(left , len(nums)):
                found.add(nums[right])

                if len(found) == total:
                    count += 1
        
        return count
