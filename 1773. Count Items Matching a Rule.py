class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for item in items:
            if ruleKey == 'type':
                if ruleValue == item[0]:
                    count += 1

            elif ruleKey == 'color':
                if ruleValue == item[1]:
                    count += 1

            elif ruleKey == 'name':
                if ruleValue == item[2]:
                    count +=1 
        return count
