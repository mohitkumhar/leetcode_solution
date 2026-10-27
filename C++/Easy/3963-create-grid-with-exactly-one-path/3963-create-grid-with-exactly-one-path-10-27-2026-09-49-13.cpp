class Solution {
public:
    vector<string> createGrid(int m, int n) {
        vector<string> result;

        for (int i = 0; i < m; i++) {
            string currStr = "";

            for (int j = 0; j < n; j++) {
                if (i == 0) {
                    currStr += '.';
                } else if (j == n - 1) {
                    currStr += '.';
                } else {
                    currStr += '#';
                }
            }
            result.push_back(currStr);
        }
        return result;
    }
};