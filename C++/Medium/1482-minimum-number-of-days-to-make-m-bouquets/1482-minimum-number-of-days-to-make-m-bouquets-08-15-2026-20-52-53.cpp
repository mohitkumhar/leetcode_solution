class Solution {
public:
    int isPossible(int day, vector<int> bloomDay, int m, int k) {
        int count = 0;
        int currBouquets = 0;

        for (int bloom : bloomDay) {
            if (bloom <= day) {
                count++;
                if (count == k) {
                    currBouquets++;
                    count = 0;
                }
            } else
                count = 0;
        }
        return currBouquets >= m;
    }
    int minDays(vector<int>& bloomDay, int m, int k) {

        if ((1LL * m * k) > bloomDay.size())
            return -1;

        int n = bloomDay.size();

        int left = *min_element(bloomDay.begin(), bloomDay.end());
        int right = *max_element(bloomDay.begin(), bloomDay.end());

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (isPossible(mid, bloomDay, m, k))
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }
};