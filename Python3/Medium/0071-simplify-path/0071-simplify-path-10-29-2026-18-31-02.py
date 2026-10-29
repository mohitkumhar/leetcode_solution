class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathList = path.split("/")

        for word in pathList:
            if word:
                if word == ".":
                    continue

                elif word == "..":
                    if stack:
                        stack.pop()

                elif word == "...":
                    stack.append(word)

                else:
                    stack.append(word)

        return "/" + "/".join(stack)
