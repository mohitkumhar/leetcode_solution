class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        # this algo dont work on january and febuary, so we add a year in month
        
        if month < 3:
            month += 12
            year -= 1

        q = day
        m = month
        K = year % 100  # year of the century
        J = year // 100   # zero-based century


        h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7

        days = ['Saturday', "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        return days[h]