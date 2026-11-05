class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        unordered_map<int, vector<pair<int, int>>> matrix;
        const int MOD = 1000000000 + 7;

        for (auto road : roads) {
            int u = road[0];
            int v = road[1];
            int w = road[2];

            matrix[u].push_back({v, w});
            matrix[v].push_back({u, w});
        }

        vector<long long> distance(n, LLONG_MAX);
        vector<int> count(n, 0);

        distance[0] = 0;
        count[0] = 1;

        priority_queue<pair<long long, int>, vector<pair<long long, int>>,
                       greater<pair<long long, int>>>
            pq;

        pq.push({0, 0}); // distance, node

        while (!pq.empty()) {
            auto [currCost, node] = pq.top();
            pq.pop();

            if (currCost > distance[node])
                continue;

            for (auto [child, cost] : matrix[node]) {
                long long newCost = currCost + cost;

                if (newCost < distance[child]) {
                    distance[child] = newCost;
                    count[child] = count[node];

                    pq.push({newCost, child});
                } else if (newCost == distance[child]) {
                    count[child] = (count[child] + count[node]) % MOD;
                }
            }
        }

        return count[n - 1];
    }
};