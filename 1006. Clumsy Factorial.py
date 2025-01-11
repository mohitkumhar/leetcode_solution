class Solution:
    def clumsy(self, n: int) -> int:
        

        ops = ['*', '//', '+', '-']
        ptr = 0
        res = ''

        for i in range(n, 1, -1):
            res += str(i)
            res += ops[ptr]
            
            ptr += 1

            if ptr == 4:
                ptr = 0
            
        return eval(res + '1')