class Solution {
public:
    bool check(int num, int row,
               const unordered_map<int, unordered_set<int>>& count) {
        return count.at(row).find(num) == count.at(row).end();
    }

    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {

        unordered_map<int, unordered_set<int>> count;

        for (auto& reservedSeat : reservedSeats) {
            int row = reservedSeat[0];
            int seat = reservedSeat[1];

            count[row].insert(seat);
        }

        int result = (n - count.size()) * 2;

        for (auto& seat : count) {
            bool group1 =
                check(2, seat.first, count) && check(3, seat.first, count) &&
                check(4, seat.first, count) && check(5, seat.first, count);
            bool group2 =
                check(4, seat.first, count) && check(5, seat.first, count) &&
                check(6, seat.first, count) && check(7, seat.first, count);
            bool group3 =
                check(6, seat.first, count) && check(7, seat.first, count) &&
                check(8, seat.first, count) && check(9, seat.first, count);

            if (group1 && group3)
                result += 2;
            else if (group1 || group2 || group3)
                result++;
        }

        return result;
    }
};