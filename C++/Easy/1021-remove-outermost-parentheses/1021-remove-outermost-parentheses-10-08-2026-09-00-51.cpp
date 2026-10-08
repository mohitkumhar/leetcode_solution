class Solution {
public:
    string removeOuterParentheses(string s) {
        int balance = 0;
        string currStr = "";

        for (char ch : s) {
            if (ch == '(') {
                if (balance > 0)
                    currStr += ch;
                balance++;
            } else {
                balance--;
                if (balance > 0)
                    currStr += ch;
            }
        }
        return currStr;
    }
};