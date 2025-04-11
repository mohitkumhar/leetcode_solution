class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for ast in asteroids:
            
            while stack and stack[-1] > 0 and ast < 0:
                
                if abs(stack[-1]) < abs(ast):
                    stack.pop()
                    continue
                
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                    break
                
                else:
                    break
            
            else:
                stack.append(ast)

            return stack
