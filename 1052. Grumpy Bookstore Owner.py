class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """

        satisfy_customer = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                satisfy_customer += customers[i]

        start = 0
        unsatisfy_customer = 0
        max_unsatisfy_customer = 0

        for end in range(len(grumpy)):

            if grumpy[end] == 1:
                unsatisfy_customer += customers[end]

            if end - start + 1 > minutes:

                if grumpy[start] == 1:
                    unsatisfy_customer -= customers[start]

                start += 1

            max_unsatisfy_customer = max(
                max_unsatisfy_customer, unsatisfy_customer)

        return max_unsatisfy_customer + satisfy_customer
