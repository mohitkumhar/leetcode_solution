class Solution {
public:
    int minimumCost(vector<int>& costs) {
        sort(costs.begin(), costs.end(), greater<int>());
        int count = 1;
        int currCost = 0;

        for (int cost : costs) {
            if (count == 3) {
                count = 1;
                continue;
            }
            currCost += cost;
            count++;
        }

        return currCost;
    }
};