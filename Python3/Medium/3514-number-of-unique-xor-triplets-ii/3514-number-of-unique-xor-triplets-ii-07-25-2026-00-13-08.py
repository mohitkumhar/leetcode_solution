class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        seen1 = set()

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                seen1.add(nums[i] ^ nums[j])

        seen2 = set()
        for pair in seen1:
            for num in nums:
                seen2.add(pair ^ num)

        return len(seen2)
