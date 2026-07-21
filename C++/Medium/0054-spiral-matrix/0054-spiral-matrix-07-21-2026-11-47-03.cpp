class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {

        int m = matrix.size();
        int n = matrix[0].size();

        int top = 0;
        int down = m - 1;

        int left = 0;
        int right = n - 1;

        vector<int> result;

        while (top <= down && left <= right) {
            // top row
            for (int i = left; i <= right; i++)
                result.push_back(matrix[top][i]);
            top++;

            // right column
            for (int i = top; i <= down; i++) {
                result.push_back(matrix[i][right]);
            }
            right--;

            // down row
            if (top <= down) {
                for (int i = right; i >= left; i--) {
                    result.push_back(matrix[down][i]);
                }
                down--;
            }

            // left column
            if (left <= right) {
                for (int i = down; i >= top; i--) {
                    result.push_back(matrix[i][left]);
                }
                left++;
            }
        }
        return result;
    }
};