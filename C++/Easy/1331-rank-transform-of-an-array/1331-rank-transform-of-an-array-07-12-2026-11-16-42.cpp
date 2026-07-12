class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        if (arr.empty())
            return {};

        set<int> unique_vals(arr.begin(), arr.end());

        unordered_map<int, int> rank_map;
        int rank = 1;
        for (int num : unique_vals) {
            rank_map[num] = rank++;
        }

        vector<int> result(arr.size());
        for (int i = 0; i < arr.size(); i++) {
            result[i] = rank_map[arr[i]];
        }

        return result;
    }
};