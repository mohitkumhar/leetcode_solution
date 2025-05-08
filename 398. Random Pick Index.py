class Solution:

    def __init__(self, nums: List[int]):
        self.count_index = {}

        for i, num in enumerate(nums):
            if num not in self.count_index:
                self.count_index[num] = []
            self.count_index[num].append(i)        

    def pick(self, target: int) -> int:
        return random.choice(self.count_index[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)