class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        set<pair<int, int>> visited;

        int count = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                if (visited.find({i, j}) != visited.end())
                    continue;
                if (grid[i][j] == 1) {

                    int groupServer = 0;
                    queue<pair<int, int>> q;

                    q.push({i, j});
                    visited.insert({i, j});

                    while (!q.empty()) {
                        auto [x, y] = q.front();
                        q.pop();

                        groupServer += 1;

                        for (int row = 0; row < m; row++) {
                            int newX = row;
                            int newY = y;

                            if (grid[newX][newY] == 1 &&
                                visited.find({newX, newY}) == visited.end()) {
                                visited.insert({newX, newY});
                                q.push({newX, newY});
                            }
                        }

                        for (int col = 0; col < n; col++) {
                            int newX = x;
                            int newY = col;

                            if (grid[newX][newY] == 1 &&
                                visited.find({newX, newY}) == visited.end()) {
                                visited.insert({newX, newY});
                                q.push({newX, newY});
                            }
                        }
                    }
                    if (groupServer > 1)
                        count += groupServer;
                }
            }
        }
        return count;
    }
};