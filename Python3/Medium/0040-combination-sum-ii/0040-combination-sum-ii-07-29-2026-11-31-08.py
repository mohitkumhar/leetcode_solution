class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(i: int, currSum: int, currComb: List[int]) -> None:
            if currSum == target:
                result.append(currComb[:])
                return

            if i >= len(candidates) or currSum > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                currSum += candidates[j]
                currComb.append(candidates[j])

                backtrack(j + 1, currSum, currComb)

                currSum -= candidates[j]
                currComb.pop()

        result = []

        candidates.sort()

        backtrack(0, 0, [])

        return result
