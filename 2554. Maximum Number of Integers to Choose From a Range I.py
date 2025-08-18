class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
      count = 0
      curr_sum = 0
      banned_set = set(banned)

      for i in range(1, n+1):
        if i not in banned_set:
          if curr_sum + i <= maxSum:
            curr_sum += i
            count += 1
      return count