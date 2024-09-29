class Solution:
    def findLucky(self, arr: List[int]) -> int:

        count = {}

        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        print(count)
        
        ans = 0

        for i in count:
            if i == count[i]:
                ans = max(ans, i)
        
        if ans is not 0:
            return ans
        return -1
