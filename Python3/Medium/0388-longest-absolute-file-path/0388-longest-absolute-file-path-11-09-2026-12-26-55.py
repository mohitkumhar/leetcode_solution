class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dirStruct = input.split("\n")
        maximum = 0
        pathMap = {0: 0}

        for dir in dirStruct:
            name = dir.lstrip("\t")
            depth = len(dir) - len(name)

            if "." in name:
                maximum = max(maximum, pathMap[depth] + len(name))
            else:
                pathMap[depth + 1] = pathMap[depth] + len(name) + 1

        return maximum
