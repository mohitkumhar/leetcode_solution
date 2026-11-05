class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        set<pair<int, int>> connected;
        vector<int> inDegree(n, 0);

        for (auto road : roads) {
            int u = road[0];
            int v = road[1];

            inDegree[u]++;
            inDegree[v]++;

            connected.insert({u, v});
            connected.insert({v, u});
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int rank = inDegree[i] + inDegree[j];

                if (connected.find({i, j}) != connected.end()) {
                    rank--;
                }
                ans = max(ans, rank);
            }
        }
        return ans;
    }
};