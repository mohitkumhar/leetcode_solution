class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int rows = matrix.size();
        int cols = matrix[0].size();

        int left = 0;
        int right = rows - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (matrix[mid][0] <= target && target <= matrix[mid][cols - 1]) {
                // search for inner col
                int l = 0;
                int r = cols - 1;

                while (l <= r) {
                    int m = l + (r - l) / 2;

                    if (matrix[mid][m] == target)
                        return true;
                    else if (matrix[mid][m] < target)
                        l = m + 1;
                    else
                        r = m - 1;
                }
                return false;
            } else if (matrix[mid][0] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return false;
    }
};