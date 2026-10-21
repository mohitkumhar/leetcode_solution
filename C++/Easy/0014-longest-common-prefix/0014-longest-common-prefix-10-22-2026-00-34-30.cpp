class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans = "";

        string minChar = *min_element(strs.begin(), strs.end());
        int minCharLen = minChar.size();

        for (int i = 0; i < minCharLen; i++) {
            char currChar = minChar[i];

            for (string str : strs) {
                if (str[i] != currChar)
                    return ans;
            }
            ans += currChar;
        }
        return ans;
    }
};