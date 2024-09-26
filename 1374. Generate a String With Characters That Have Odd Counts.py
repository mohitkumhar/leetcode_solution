class Solution:
    def generateTheString(self, n: int) -> str:
        ans = ''

        if n % 2 == 1:
            ans = 'a' * n
        else:
            ans = 'a' * (n - 1)
            ans += 'b'

        
        return ans
