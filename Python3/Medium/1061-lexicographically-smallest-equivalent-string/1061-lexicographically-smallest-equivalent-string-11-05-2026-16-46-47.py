class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        def find(target):
            if target == parent[target]:
                return target

            else:
                parent[target] = find(parent[target])
                return parent[target]

        def union(a, b):
            aParent = find(a)
            bParent = find(b)

            if aParent < bParent:
                parent[bParent] = aParent
            else:
                parent[aParent] = bParent

        n = len(s1)
        parent = {}

        for i in range(26):
            parent[chr(i + ord("a"))] = chr(i + ord("a"))

        for i in range(n):
            union(s1[i], s2[i])

        smallestStr = ""

        for char in baseStr:
            smallerChar = find(char)
            smallestStr += smallerChar

        return smallestStr
