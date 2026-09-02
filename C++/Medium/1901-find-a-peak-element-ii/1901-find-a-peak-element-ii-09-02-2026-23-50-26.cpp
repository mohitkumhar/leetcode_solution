#include <iterator>

class Solution {
public:
    vector<int> findPeakGrid(vector<vector<int>>& mat) {

        int m = mat.size();
        int n = mat[0].size();

        int left = 0;
        int right = m - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            auto maxElement = max_element(mat[mid].begin(), mat[mid].end());
            int maxColElementIdx = distance(mat[mid].begin(), maxElement);

            int top = mid > 0 ? mat[mid - 1][maxColElementIdx] : -1;
            int bottom = mid < m - 1 ? mat[mid + 1][maxColElementIdx] : -1;

            if (mat[mid][maxColElementIdx] > top &&
                mat[mid][maxColElementIdx] > bottom)
                return {mid, maxColElementIdx};

            else if (mat[mid][maxColElementIdx] < top)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return {-1, -1};
    }
};