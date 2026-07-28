class Solution {
public:
    string longestPrefix(string s) {
        int n = s.size();

        vector<int> LPS(n, 0);
        LPS[0] = 0;
        int length_idx = 0;

        int i = 1;

        while (i < n) {
            if (s[i] == s[length_idx]) {
                length_idx++;
                LPS[i] = length_idx;
                i++;

            } else {
                if (length_idx > 0)
                    length_idx = LPS[length_idx - 1];
                else {
                    LPS[i] = 0;
                    i++;
                }
            }
        }
        return s.substr(0, LPS[n - 1]);
    }
};