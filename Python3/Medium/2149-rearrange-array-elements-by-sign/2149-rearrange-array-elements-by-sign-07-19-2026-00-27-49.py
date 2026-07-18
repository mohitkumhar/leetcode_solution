class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_ele = []
        negative_ele = []

        for num in nums:
            if num > 0:
                positive_ele.append(num)
            else:
                negative_ele.append(num)

        i = 0
        j = 0
        result = []

        while i < len(positive_ele):
            result.append(positive_ele[i])
            result.append(negative_ele[j])
            i += 1
            j += 1

        return result
