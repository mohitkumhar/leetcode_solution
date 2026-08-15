class Solution {
public:
    bool isPossible(int maxWeight, vector<int>& weights, int days) {
        int currWeight = 0;
        int currDays = 1;

        for (int weight : weights) {
            if ((currWeight + weight) > maxWeight) {
                currDays++;
                currWeight = weight;
            } else
                currWeight += weight;
        }

        return currDays <= days;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int left = *max_element(weights.begin(), weights.end());
        int right = accumulate(weights.begin(), weights.end(), 0);

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (isPossible(mid, weights, days))
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }
};