class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        count = {}

        for i in hand:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        sorted_count = sorted(count.keys())

        for card in sorted_count:
            while count[card] > 0:
                for i in range(groupSize):
                    if card + i not in count or count[card + i] == 0:
                        return False

                    count[card + i] -= 1

        return True
