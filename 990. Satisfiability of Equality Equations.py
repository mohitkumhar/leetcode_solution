class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(28)]

        def find(target):
            if target == parent[target]:
                return target
            
            else:
                return find(parent[target])

        def union(a, b, sign):
            a_parent = find(a)
            b_parent = find(b)

            if sign == "==":
                if a_parent == b_parent:
                    return True

                parent[b_parent] = a_parent

            else:
                print("in, else: ", sign, a_parent, b_parent)
                if a_parent == b_parent:
                    return False
        
        for equation in equations:
            a = equation[0]
            b = equation[-1]

            sign = equation[1:-1]
            
            a = ord(a) - 97
            b = ord(b) - 97

            if sign == "==":
                union(a, b, sign)
        
        for equation in equations:
            a = equation[0]
            b = equation[-1]

            sign = equation[1:-1]

            if sign == "!=":
                a = ord(a) - 97
                b = ord(b) - 97

                a_parent = find(a)
                b_parent = find(b)

                if a_parent == b_parent:
                    return False

        return True
