class Solution:
    def convertDateToBinary(self, date: str) -> str:

        dates = date.split('-')
        result = []
        
        for date in dates:

            binary_date = bin(int(date))
            result.append(binary_date[2:])

        return '-'.join(result)
        