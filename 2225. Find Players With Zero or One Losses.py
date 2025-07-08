class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer0 = []
        answer1 = []
        count = {}

        for match in matches:
            if match[1] in count:
                count[match[1]] += 1
            else:
                count[match[1]] = 1

        for match in matches:
            if match[0] not in count:
                answer0.append(match[0])

        result0 = sorted(count.items(), key=lambda x: x[1])
        for result in result0:
            if result[1] == 1:
                answer1.append(result[0])

        return [sorted(set(answer0)), sorted(answer1)]
