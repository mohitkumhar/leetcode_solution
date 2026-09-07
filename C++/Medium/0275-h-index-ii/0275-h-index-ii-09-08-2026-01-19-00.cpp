class Solution {
public:
    bool isPossible(int maxVal, vector<int>& citations) {
        int count = 0;
        for (int num : citations) {
            if (num >= maxVal)
                count++;
            if (count >= maxVal)
                return true;
        }
        return false;
    }

    int hIndex(vector<int>& citations) {

        int left = 1;
        int right = *max_element(citations.begin(), citations.end());
        int result = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (isPossible(mid, citations)) {
                result = mid;
                left = mid + 1;
            } else
                right = mid - 1;
        }
        return result;
    }
};