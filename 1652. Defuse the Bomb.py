class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans

        for i in range(n):
            total = 0
            if k > 0:
                idx = i + 1
                for _ in range(k):
                    if idx == n:
                        idx = 0
                    total += code[idx]
                    idx += 1

            else:
                idx = i - 1
                for _ in range(-k):
                    if idx == -1:
                        idx = n - 1
                    total += code[idx]
                    idx -= 1

            ans[i] = total
        return ans
