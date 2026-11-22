class Solution {
public:
    bool checkString(string s) {
        bool flag = false;

        for (char ch : s) {
            if (ch == 'b') {
                flag = true;
            } else if (ch == 'a' && flag) {
                return false;
            }
        }
        return true;
    }
};