class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        int minWordLen = INT_MAX;

        for (string str : strs)
            minWordLen = min(minWordLen, (int)str.size());

        for (int i = 0; i < minWordLen; i++) {
            char currChar = strs[0][i];

            for (string s : strs) {
                if (s[i] != currChar)
                    return strs[0].substr(0, i);
            }
        }
        return strs[0].substr(0, minWordLen);
    }
};