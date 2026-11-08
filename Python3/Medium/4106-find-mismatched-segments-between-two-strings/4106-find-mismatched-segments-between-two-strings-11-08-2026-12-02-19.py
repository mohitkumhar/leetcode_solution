class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        i = 0
        j = 0

        n = len(s1)

        currMatch1 = ""
        currMatch2 = ""
        result = []

        while i < n:
            if s1[i] == s2[j]:
                if currMatch1 and currMatch2:
                    result.append([currMatch1, currMatch2])
                currMatch1 = ""
                currMatch2 = ""

            else:
                currMatch1 += s1[i]
                currMatch2 += s2[j]

            i += 1
            j += 1
            
        if currMatch1 and currMatch2:
            result.append([currMatch1, currMatch2])

        return result
