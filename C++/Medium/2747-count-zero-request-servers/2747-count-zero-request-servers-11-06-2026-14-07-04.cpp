class Solution {
public:
    vector<int> countServers(int n, vector<vector<int>>& logs, int x,
                             vector<int>& queries) {
        int m = logs.size();

        auto lambda = [](vector<int>& vec1, vector<int>& vec2) {
            return vec1[1] < vec2[1];
        };

        sort(begin(logs), end(logs), lambda);

        vector<pair<int, int>> query(queries.size());
        for (int i = 0; i < queries.size(); i++) {
            query[i] = {queries[i], i};
        }

        sort(query.begin(), query.end());

        unordered_map<int, int> freq;
        vector<int> result(queries.size());

        int i = 0;
        int j = 0;

        for (auto [time, idx] : query) {
            int start = time - x;
            int end = time;

            while (j < m && logs[j][1] <= end) {
                freq[logs[j][0]]++;
                j++;
            }

            while (i < m && logs[i][1] < start) {
                freq[logs[i][0]]--;
                if (freq[logs[i][0]] == 0)
                    freq.erase(logs[i][0]);
                i++;
            }
            int remainingServers = n - freq.size();
            result[idx] = remainingServers;
        }
        return result;
    }
};