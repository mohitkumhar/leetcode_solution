class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        def backtrack(i, curr_comb, map):
            nonlocal count

            if i >= len(nums):
                count += 1
                return

            # skip
            backtrack(i + 1, curr_comb, map)

            # take
            if nums[i] + k not in map and nums[i] - k not in map:
                map[nums[i]] = map.get(nums[i], 0 ) + 1
                curr_comb.append(nums[i])

                backtrack(i + 1, curr_comb, map)

                curr_comb.pop()
                map[nums[i]] -= 1
                if map[nums[i]] == 0:
                    del map[nums[i]]

        count = 0

        backtrack(0, [], {})

        return count - 1 # since it count the empty subset
