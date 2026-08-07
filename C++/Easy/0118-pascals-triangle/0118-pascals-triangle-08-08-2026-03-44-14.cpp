class Solution {
public:
    vector<vector<int>> generate(int numRows) {

        if (numRows == 1)
            return {{1}};

        else if (numRows == 2)
            return {{1}, {1, 1}};

        vector<vector<int>> result = {{1}, {1, 1}};

        vector<int> prev = {1, 1};

        for (int i = 3; i <= numRows; i++) {
            vector<int> currRow = {1};
            int j = 1;

            while (j < prev.size()) {
                currRow.push_back(prev[j - 1] + prev[j]);
                j++;
            }
            currRow.push_back(1);

            result.push_back(currRow);
            prev = currRow;
        }

        return result;
    }
};