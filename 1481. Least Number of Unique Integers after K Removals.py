class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        count = dict(sorted(count.items(), key=lambda x: x[1]))
        ans = 0
        for key, val in count.items():
            if k <= 0:
                ans += 1
                continue
            while val >= 1 and k >= 1:
                val -= 1
                k -= 1
            if val > 0 and k == 0:
                ans += 1

        return ans
