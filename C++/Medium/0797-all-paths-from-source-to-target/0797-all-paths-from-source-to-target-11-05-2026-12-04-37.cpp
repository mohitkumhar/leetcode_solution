class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int n = graph.size();

        queue<pair<int, vector<int>>> q;
        q.push({0, {0}});
        vector<vector<int>> result;

        while (!q.empty()) {
            auto [node, path] = q.front();
            q.pop();

            if (node == n - 1)
                result.push_back(path);

            for (int nei : graph[node]) {
                vector<int> newPath = path;
                newPath.push_back(nei);

                q.push({nei, newPath});
            }
        }
        return result;
    }
};