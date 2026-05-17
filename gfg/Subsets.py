class Solution:
    def subsets(self, arr):
        result = []
        n = len(arr)
        
        def solve(i, temp):
            if i == n:
                result.append(temp[:])
                return None

            # take element
            temp.append(arr[i])
            solve(i + 1, temp)
            temp.pop()
            
            # skip element
            solve(i + 1, temp)


        solve(0, [])
        
        return result
