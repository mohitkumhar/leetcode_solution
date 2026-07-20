class Solution {
public:
    void reverse(vector<int>& nums, int i, int j) {
        while (i < j) {
            swap(nums[i], nums[j]);
            i++;
            j--;
        }
    }

    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        vector<int> flattenGrid;
        int m = grid.size();
        int n = grid[0].size();
        k %= (m * n);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                flattenGrid.push_back(grid[i][j]);
            }
        }

        reverse(flattenGrid, 0, m * n - 1);
        reverse(flattenGrid, 0, k - 1);
        reverse(flattenGrid, k, m * n - 1);

        int idx = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = flattenGrid[idx++];
            }
        }

        return grid;
    }
};