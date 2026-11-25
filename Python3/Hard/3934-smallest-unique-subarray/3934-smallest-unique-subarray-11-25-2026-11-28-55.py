class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        names = [nums]
        for k in range(n.bit_length() - 1):
            ids = {}
            names.append(
                [
                    ids.setdefault(pair, len(ids))
                    for pair in zip(names[k], names[k][2**k :])
                ]
            )

        def found(length):
            k = length.bit_length() - 1
            return 1 in Counter(zip(names[k], names[k][length - 2**k :])).values()

        return bisect_left(range(1, n), True, key=found) + 1
