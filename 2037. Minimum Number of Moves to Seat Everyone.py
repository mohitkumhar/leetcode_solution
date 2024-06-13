class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """

        total_moves = 0

        students.sort()
        seats.sort()

        for student, seat in zip(students, seats):
            total_moves = total_moves + abs(student - seat)

        return total_moves
