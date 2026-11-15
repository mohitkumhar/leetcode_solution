class Solution {
public:
    string reverseWords(string s) {
        vector<string> str;
        string currStr = "";

        for (char ch : s) {
            if (ch != ' ') {
                currStr += ch;
            } else if (currStr != "") {
                str.push_back(currStr);
                currStr = "";
            }
        }

        if (currStr != "")
            str.push_back(currStr);

        string result = "";
        for (int i = str.size() - 1; i >= 0; i--) {
            result += str[i];
            if (i > 0)
                result += " ";
        }

        return result;
    }
};