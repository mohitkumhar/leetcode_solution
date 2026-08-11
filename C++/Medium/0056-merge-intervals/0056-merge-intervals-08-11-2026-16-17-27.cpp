class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {

        sort(intervals.begin(), intervals.end());

        vector<vector<int>> result;

        for (auto& interval : intervals) {
            int n = result.size();

            if (result.empty() || result[n - 1][1] < interval[0])
                result.push_back({interval[0], interval[1]});
            else
                result[n - 1][1] = max(result[n - 1][1], interval[1]);
        }

        return result;
    }
};