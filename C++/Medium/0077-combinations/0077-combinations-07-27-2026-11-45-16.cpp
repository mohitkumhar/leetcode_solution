class Solution {
public:
    void backtrack(int i, vector<int>& curr_comb, vector<vector<int>>& result,
                   int n, int k) {
        if (curr_comb.size() == k) {
            result.push_back(curr_comb);
            return;
        }
        if (i == (n + 1))
            return;

        for (int j = i; j <= n; j++) {
            curr_comb.push_back(j);

            backtrack(j + 1, curr_comb, result, n, k);

            curr_comb.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> curr_comb;

        backtrack(1, curr_comb, result, n, k);

        return result;
    }
};