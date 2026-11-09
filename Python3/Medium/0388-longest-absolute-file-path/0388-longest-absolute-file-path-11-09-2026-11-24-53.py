class Solution:
    def lengthLongestPath(self, input: str) -> int:

        lines = input.split("\n")

        pathMap = {0: 0}

        stack = []
        longest = 0

        for line in lines:

            name = line.lstrip("\t")
            depth = len(line) - len(name)

            if "." in name:
                longest = max(longest, pathMap[depth] + len(name))
            else:
                pathMap[depth + 1] = pathMap[depth] + len(name) + 1

        return longest
