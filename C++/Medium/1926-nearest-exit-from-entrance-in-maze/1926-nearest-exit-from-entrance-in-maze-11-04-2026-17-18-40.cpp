class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {

        int m = maze.size();
        int n = maze[0].size();

        queue<tuple<int, int, int>> q;
        q.push({entrance[0], entrance[1], 0});

        vector<vector<bool>> visited(m, vector<bool>(n, false));
        visited[entrance[0]][entrance[1]] = true;

        vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        while (!q.empty()) {
            auto [x, y, dist] = q.front();
            q.pop();

            if (dist > 0 && (x == m - 1 || x == 0 || y == n - 1 || y == 0)) {
                return dist;
            }

            for (pair<int, int> direction : directions) {
                int newX = x + direction.first;
                int newY = y + direction.second;

                if (0 <= newX && newX < m && 0 <= newY && newY < n) {
                    if (!visited[newX][newY]) {
                        if (maze[newX][newY] == '.') {
                            visited[newX][newY] = true;
                            q.push({newX, newY, dist + 1});
                        }
                    }
                }
            }
        }
        return -1;
    }
};