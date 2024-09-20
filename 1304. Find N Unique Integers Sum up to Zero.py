class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n % 2 == 1:
            for i in range(-n//2 + 1, n//2 + 1):
                print('i is: ',i)
                ans.append(i)
        else:
            for i in range(-n//2, n//2 + 1):
                print('i is: ',i)
                if i == 0:
                    continue
                else:
                    ans.append(i)
        return ans