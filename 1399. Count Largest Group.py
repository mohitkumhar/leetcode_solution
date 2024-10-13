class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        def getSum(value):
            nums = str(value)
            sum = 0
            for num in nums:
                sum += int(num)

            return sum

        count = {}


        for i in range(1, n + 1):
            value = getSum(i)

            if value in count:
                count[value] += 1
            else:
                count[value] = 1
            

        max_value = max(count.values())

        group = 0
        for key, value in count.items():
            if value == max_value:
                group += 1
        
        return group
