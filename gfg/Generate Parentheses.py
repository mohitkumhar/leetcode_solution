class Solution:
    def generateParentheses(self, n):
        result = []
        
        def is_valid(string):
            count = 0
            for char in string:
                if char == "(":
                    count += 1
                else:
                    count -= 1
                
                if count < 0:
                    return False
            
            return count == 0
        
        def solve(string):
            if len(string) == n:
                if is_valid(string):
                    result.append("".join(string))
                return
        
            string.append("(")
            solve(string)
            string.pop()
        
            string.append(")")
            solve(string)
            string.pop()

        solve([])
        return result
        
