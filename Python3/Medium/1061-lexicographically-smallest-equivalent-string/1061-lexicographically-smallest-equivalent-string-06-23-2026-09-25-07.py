class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(target):
            if target == parent[target]:
                return target
            else:
                parent[target] = find(parent[target])
                return parent[target]

        def union(a, b):
            a_parent = find(a)
            b_parent = find(b)

            if a_parent != b_parent:
                if a_parent < b_parent:
                    parent[b_parent] = a_parent
                elif a_parent > b_parent:
                    parent[a_parent] = b_parent

        n = len(s1)
        parent = {}
        for char in range(26):
            parent[chr(char + 97)] = chr(char + 97)

        for i in range(n):
            union(s1[i], s2[i])

        ans = ''
        for char in baseStr:
            smaller_char = find(char)
            ans += smaller_char

        return ans
