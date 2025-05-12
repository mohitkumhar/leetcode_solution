class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequent(a, b):
            i = 0
            for char in b:
                if i < len(a) and a[i] == char:
                    i += 1
            return i == len(a)

        strs.sort(key=len, reverse=True)
    
        for i, s in enumerate(strs):
            if all(not is_subsequent(s, strs[j]) for j in range(len(strs)) if j != i):
                return len(s)

        return -1
