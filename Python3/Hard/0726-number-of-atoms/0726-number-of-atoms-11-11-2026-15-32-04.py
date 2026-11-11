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
                i += 1  # moving forward from ')

                num = 0
                while i < n and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1

                if num == 0:
                    num = 1

                for atom, count in curr.items():
                    stack[-1][atom] = stack[-1].get(atom, 0) + count * num

            else:
                # normal formula or atom count

                start = i
                i += 1  # for start letter of formula (capital letter)

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

        ans = ""
        for atom in sorted(stack[-1]):
            ans += atom

            if stack[-1][atom] > 1:
                ans += str(stack[-1][atom])

        return ans
