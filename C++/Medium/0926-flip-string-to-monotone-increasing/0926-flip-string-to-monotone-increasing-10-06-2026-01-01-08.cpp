class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int countOne = 0;
        int flip = 0;

        for (char ch : s) {
            if (ch == '1')
                countOne++;
            else {
                flip++;
                flip = min(flip, countOne);
            }
        }
        return flip;
    }
};