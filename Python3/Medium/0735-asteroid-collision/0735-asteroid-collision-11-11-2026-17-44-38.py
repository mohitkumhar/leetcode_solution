class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for ast in asteroids:
            destroyed = False

            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] < abs(ast):
                    stack.pop()
                elif stack[-1] == abs(ast):
                    destroyed = True
                    stack.pop()
                    break
                else:
                    destroyed = True
                    break

            if not destroyed:
                stack.append(ast)

        return stack
