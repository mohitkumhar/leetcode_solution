class Solution:
    def average(self, salary: List[int]) -> float:
        arr = sorted(salary)[1:-1]
        return sum(arr)/ len(arr)