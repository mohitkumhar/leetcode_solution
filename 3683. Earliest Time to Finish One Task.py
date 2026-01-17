class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = []
        for task in tasks:
            ans.append(task[0] + task[1])
        return min(ans)
