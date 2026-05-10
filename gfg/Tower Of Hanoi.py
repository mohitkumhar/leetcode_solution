class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        
        
        def solve(n, fromm, to, aux):
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            count = solve(n - 1, fromm , aux, to)
            count += 1
            
            count += solve(n - 1, aux, to, fromm)
        
            return count
        
        return solve(n, fromm, to, aux)
