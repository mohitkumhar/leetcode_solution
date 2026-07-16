class Solution:
    def __init__(self):
        self.visited = set()
        self.result = []

    def backtrack(self, temp: List[int], nums: List[int]) -> None:
        if len(temp) == len(nums):
            self.result.append(temp[:])
            return None

        for i in range(len(nums)):
            if i in self.visited:
                continue

            self.visited.add(i)
            temp.append(nums[i])

            self.backtrack(temp, nums)

            temp.pop()
            self.visited.remove(i)

    def permute(self, nums: List[int]) -> List[List[int]]:

        self.backtrack([], nums)
        return self.result
