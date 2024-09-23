class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        def no_zero(num):
            num_str = str(num)
            if '0' in num_str:
                return 1
            return 0
        
        ans = []


        for i in range(n):
            if no_zero(i) or no_zero(n - i):
                continue
            else:
                ans.append(i)
                ans.append(n - i)
                break
        
        return ans