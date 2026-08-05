class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        int top = 0;
        int bottom = m - 1;
        int left = 0;
        int right = n - 1;

        vector<int> result;

        while ((top <= bottom) && (left <= right)) {
            // top row
            for (int i = left; i <= right; i++)
                result.push_back(matrix[top][i]);
            top++;

            // right col
            for (int i = top; i <= bottom; i++)
                result.push_back(matrix[i][right]);
            right--;

            // bottom row
            if (top <= bottom) {
                for (int i = right; i >= left; i--)
                    result.push_back(matrix[bottom][i]);
                bottom--;
            }

            // left col
            if (right >= left) {
                for (int i = bottom; i >= top; i--)
                    result.push_back(matrix[i][left]);
                left++;
            }
        }
        return result;
    }
};