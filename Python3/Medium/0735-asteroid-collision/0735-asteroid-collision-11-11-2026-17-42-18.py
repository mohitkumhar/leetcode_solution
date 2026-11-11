class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for ast in asteroids:

            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] < abs(ast):
                    stack.pop()
                elif stack[-1] == abs(ast):
                    stack.pop()
                    break
                else:
                    break

            else:
                stack.append(ast)

        return stack
