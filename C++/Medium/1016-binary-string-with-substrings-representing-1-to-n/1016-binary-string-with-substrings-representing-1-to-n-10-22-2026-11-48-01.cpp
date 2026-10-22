class Solution {
public:
    bool queryString(string s, int n) {
        for (int i = 1; i <= n; i++) {
            string num = "";

            int x = i;

            while (x > 0) {
                num = char('0' + (x % 2)) + num;
                x /= 2;
            }
            if (s.find(num) == string::npos) {
                return false;
            }
        }
        return true;
    }
};