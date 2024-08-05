class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        ans = [i for i in count if count[i] == 1]
        print(ans)

        try:
            return ans[k - 1]
        except:
            return ''
