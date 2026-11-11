class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:

        robots = []  # position, health, direction, idx
        stack = []
        n = len(positions)

        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])

        for robot in sorted(robots):
            destroyed = False

            while stack and stack[-1][2] == "R" and robot[2] == "L":

                if stack[-1][1] == robot[1]:
                    destroyed = True
                    stack.pop()
                    break

                elif stack[-1][1] < robot[1]:
                    stack.pop()
                    robot[1] -= 1

                else:
                    # stack[-1][1] > robot[1]
                    destroyed = True
                    stack[-1][1] -= 1
                    break

            if not destroyed:
                stack.append(robot)

        stack.sort(key=lambda x: x[3])

        return [ans[1] for ans in stack]
