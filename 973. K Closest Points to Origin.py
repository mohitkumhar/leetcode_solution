import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      result = []
      for point in points:
        a = math.sqrt((point[0] - 0)**2 + (point[1])**2 - 0)
        result.append((point, a))
      result.sort(key= lambda x: x[1])

      ans = []
      for res in result:
        ans.append(res[0])
        if len(ans) == k:
          break
      return ans