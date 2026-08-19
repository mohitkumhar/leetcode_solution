class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks,
                    int additionalRocks) {

        int n = rocks.size();
        vector<int> differenceArray;
        int count = 0;

        for (int i = 0; i < n; i++) {
            differenceArray.push_back(capacity[i] - rocks[i]);
        }

        sort(differenceArray.begin(), differenceArray.end());

        for (int diff : differenceArray) {
            if (additionalRocks < diff)
                break;

            if (diff == 0) {
                count++;
                continue;
            }

            additionalRocks -= diff;
            count += 1;
        }

        return count;
    }
};