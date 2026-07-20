class Solution {
public:
    int findSmallerKValues(int val, int n, vector<vector<int>> matrix) {
        int i = n - 1;
        int j = 0;
        int count = 0;

        while (i >= 0 && j < n) {
            if (matrix[i][j] <= val) {
                count += i + 1;
                j++;
            } else
                i--;
        }
        return count;
    }

    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();

        // smallest value in matrix
        int left = matrix[0][0];

        // largest value in matrix
        int right = matrix[n - 1][n - 1];

        while (left < right) {
            int mid = left + (right - left) / 2;

            int smallerKValues = findSmallerKValues(mid, n, matrix);

            if (smallerKValues >= k)
                right = mid;

            else
                left = mid + 1;
        }
        return left;
    }
};