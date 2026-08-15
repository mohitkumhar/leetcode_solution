class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int left = 0;
        int right = arr.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            int missingCount = arr[mid] - (mid + 1);

            if (missingCount >= k)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return left + k;
    }
};