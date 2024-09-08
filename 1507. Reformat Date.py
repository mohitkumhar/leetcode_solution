class Solution:
    def reformatDate(self, date: str) -> str:

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        day, month, year = date.split()

        day = day[:-2].zfill(2)
        print(day)

        month = str(months.index(month) + 1) .zfill(2)
        print(month)
        
        ans = year + '-' + month + '-' + day
        
        return ans