from datetime import date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        f_date = date1.split('-')
        s_date = date2.split('-')
        
        year1 = int(f_date[0])
        month1 = int(f_date[1])
        day1 = int(f_date[2])

        start = date(year1, month1, day1)
        
        
        year2 = int(s_date[0])
        month2 = int(s_date[1])
        day2 = int(s_date[2])
        end = date(year2, month2, day2)

        delta = end - start
        print(delta)

        return abs(delta.days)