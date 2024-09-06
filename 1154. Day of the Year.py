class Solution:
    def dayOfYear(self, date: str) -> int:

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        year, month, day = map(int, date.split('-'))

        # check if leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            months[1] = 29

        return sum(months[:month - 1]) + day
        