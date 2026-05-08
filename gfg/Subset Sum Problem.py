class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        memo = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]
        
        def solve(i, curr_sum):
            if memo[i][curr_sum] != -1:
                return memo[i][curr_sum]

            if curr_sum == sum:
                return True
                
            if i >= n or curr_sum > sum:
                return False
            
            
            take = False
            if arr[i] + curr_sum <= sum:
                take = solve(i + 1, curr_sum + arr[i])
            
            skip = solve(i + 1, curr_sum)
            
            memo[i][curr_sum] = take or skip
            
            return take or skip
        
        return solve(0, 0)
            
