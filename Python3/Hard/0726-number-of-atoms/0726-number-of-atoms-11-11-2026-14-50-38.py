class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [{}]
        n = len(formula)
        i = 0

        while i < n:

            if formula[i] == "(":
                stack.append({})
                i += 1

            elif formula[i] == ")":
                curr = stack.pop()
                i += 1

                num = 0
                while i < n and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1

                if num == 0:
                    num = 1

                if stack:
                    for atom, count in curr.items():
                        stack[-1][atom] = stack[-1].get(atom, 0) + count * num

            else:
                # handle the formulas and count

                start = i
                i += 1

                while i < n and formula[i].islower():
                    i += 1

                atom = formula[start:i]

                num = 0
                while i < n and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1

                if num == 0:
                    num = 1

                stack[-1][atom] = stack[-1].get(atom, 0) + num

        ans = []

        for atom in sorted(stack[0]):
            ans.append(atom)

            if stack[0][atom] > 1:
                ans.append(str(stack[0][atom]))

        return "".join(ans)
