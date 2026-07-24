class Solution {
public:
    bool isPal(string s, int i, int j) {
        string temp = s.substr(i, j - i + 1);
        string rev = temp;
        reverse(rev.begin(), rev.end());

        return temp == rev;
    }

    void backtrack(int i, vector<string>& temp, vector<vector<string>>& result,
                   string s) {
        if (i == s.size()) {
            result.push_back(temp);
            return;
        }

        for (int j = i; j < s.size(); j++) {
            if (!isPal(s, i, j))
                continue;
            temp.push_back(s.substr(i, j - i + 1));

            backtrack(j + 1, temp, result, s);

            temp.pop_back();
        }
    }

    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> temp;

        backtrack(0, temp, result, s);

        return result;
    }
};