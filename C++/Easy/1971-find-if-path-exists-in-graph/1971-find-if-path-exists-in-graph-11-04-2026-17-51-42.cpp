class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source,
                   int destination) {
        unordered_map<int, vector<int>> matrix;
        unordered_set<int> visited;

        for (auto edge : edges) {
            int u = edge[0];
            int v = edge[1];

            matrix[u].push_back(v);
            matrix[v].push_back(u);
        }

        queue<int> q;
        q.push(source);

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            if (u == destination)
                return true;

            for (int v : matrix[u]) {
                if (visited.find(v) == visited.end()) {
                    visited.insert(v);
                    q.push(v);
                }
            }
        }

        return false;
    }
};