class Solution {
public:
    unordered_map<char, int> dfs(int node, int parent,
                                 unordered_map<int, vector<int>>& matrix,
                                 string& labels, vector<int>& answer) {

        unordered_map<char, int> freq;
        freq[labels[node]]++;

        for (int child : matrix[node]) {
            if (child == parent)
                continue;

            unordered_map<char, int> freqFromChild =
                dfs(child, node, matrix, labels, answer);

            for (auto& it : freqFromChild)
                freq[it.first] += it.second;
        }
        answer[node] = freq[labels[node]];
        return freq;
    }

    vector<int> countSubTrees(int n, vector<vector<int>>& edges,
                              string labels) {

        unordered_map<int, vector<int>> matrix;

        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];

            matrix[u].push_back(v);
            matrix[v].push_back(u);
        }

        vector<int> answer(n, 0);

        dfs(0, -1, matrix, labels, answer);

        return answer;
    }
};