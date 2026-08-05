class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (j >= i)
                    swap(matrix[i][j], matrix[j][i]);

        for (vector<int>& mat : matrix)
            reverse(mat.begin(), mat.end());
    }
};