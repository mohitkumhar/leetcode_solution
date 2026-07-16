class Solution:
    def __init__(self):
        self.result = []
        self.counter = {}
        self.n = 0

    def backtrack(self, temp):
        if len(temp) == self.n:
            self.result.append(temp[:])
            return

        for num in self.counter:
            if self.counter[num] >= 1:
                self.counter[num] -= 1
                temp.append(num)

                self.backtrack(temp)

                temp.pop()
                self.counter[num] += 1

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        for num in nums:
            self.counter[num] = self.counter.get(num, 0) + 1

        self.n = len(nums)
        self.backtrack([])
        return self.result
