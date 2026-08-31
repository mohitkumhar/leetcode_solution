class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {

        int n = cardPoints.size();
        long long total = accumulate(cardPoints.begin(), cardPoints.end(), 0LL);

        if (k == n) return total;

        int i = 0;
        long long currSum = 0;
        long long ans = LLONG_MAX;
        int windowSize = n - k;

        for (int j = 0; j < n; j++) {
            currSum += cardPoints[j];

            if (j - i + 1 == windowSize) {
                ans = min(ans, currSum);

                currSum -= cardPoints[i];
                i++;
            }
        }

        return total - ans;
    }
};