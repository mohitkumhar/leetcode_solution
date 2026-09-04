class Solution {
public:
    string largestOddNumber(string num) {
        int n = num.size();
        int j = n - 1;

        while (j >= 0) {
            if ((num[j] - '0') % 2 == 1) {
                return num.substr(0, j + 1);
            }
            j--;
        }
        return "";
    }
};