class Solution {
public:
    bool isPalindrome(string s) {
        string currStr = "";

        for (char ch : s) {
            if (isalnum(ch))
                currStr += tolower(ch);
        }
        string revStr = currStr;
        reverse(revStr.begin(), revStr.end());

        return currStr == revStr;
    }
};