class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_map = {}
        result = []

        for i, size in enumerate(groupSizes):
            if size not in group_map:
                group_map[size] = []
            group_map[size].append(i)

            if len(group_map[size]) == size:
                result.append(group_map[size])
                group_map[size] = []

        return result
