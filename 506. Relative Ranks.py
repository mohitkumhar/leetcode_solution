class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        sorted_score = sorted(score, reverse = True)

        rank_mapping = {}

        for i in range(len(score)):
            if i + 1 == 1:
                rank_mapping[sorted_score[i]] = 'Gold Medal'
            
            elif i + 1 == 2:
                rank_mapping[sorted_score[i]] = 'Silver Medal'
            
            elif i + 1 == 3:
                rank_mapping[sorted_score[i]] = 'Bronze Medal'
            
            else:
                rank_mapping[sorted_score[i]] = str(i + 1)
            
        rank = [rank_mapping[i] for i in score]

        return rank
