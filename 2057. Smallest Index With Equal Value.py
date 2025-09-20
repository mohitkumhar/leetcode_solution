class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        check = []
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                check.append(i)
        return check[0] if check else -1