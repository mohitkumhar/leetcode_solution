class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:

        robots = []
        n = len(positions)

        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])

        robots.sort()  # position, health, direction

        stack = []

        for robot in robots:
            destroyed = False

            while stack and stack[-1][2] == "R" and robot[2] == "L":

                if stack[-1][1] < robot[1]:
                    stack.pop()
                    robot[1] -= 1

                elif stack[-1][1] == robot[1]:
                    destroyed = True
                    stack.pop()
                    break
                else:
                    destroyed = True
                    stack[-1][1] -= 1
                    break

            if not destroyed:
                stack.append(robot)

        ans = []

        for robot, health, dir, i in sorted(stack, key=lambda x: x[3]):
            ans.append(health)

        return ans
