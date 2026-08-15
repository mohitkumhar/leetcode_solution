class Solution {
public:
    bool canEat(int hr, vector<int> piles, int h) {

        long long currHours = 0;

        for (int pile : piles) {
            currHours += pile / hr;

            if (pile % hr != 0)
                currHours += 1;
        }
        return currHours <= h;
    }
    int minEatingSpeed(vector<int>& piles, int h) {

        int n = piles.size();

        int left = 1;
        int right = *max_element(piles.begin(), piles.end());

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (canEat(mid, piles, h))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
};