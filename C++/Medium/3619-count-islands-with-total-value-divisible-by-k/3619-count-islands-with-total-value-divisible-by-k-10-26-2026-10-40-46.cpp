class Solution {
public:
    int countIslands(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        set<pair<int, int>> seen;
        int count = 0;

        vector<pair<int, int>> directions = {{1, 0}, {0, 1}, {0, -1}, {-1, 0}};

        for (int i = 0; i < m; i++) {
            queue<pair<int, int>> q;

            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 0 && seen.find({i, j}) == seen.end()) {
                    q.push({i, j});
                    seen.insert({i, j});
                    long long total = 0;

                    while (!q.empty()) {
                        auto [x, y] = q.front();
                        q.pop();

                        total += grid[x][y];

                        for (auto& direction : directions) {
                            int newX = x + direction.first;
                            int newY = y + direction.second;

                            if (0 <= newX && newX < m && 0 <= newY &&
                                newY < n) {
                                if (grid[newX][newY] != 0 &&
                                    seen.find({newX, newY}) == seen.end()) {
                                    seen.insert({newX, newY});
                                    q.push({newX, newY});
                                }
                            }
                        }
                    }
                    if (total % k == 0)
                        count++;
                }
            }
        }
        return count;
    }
};