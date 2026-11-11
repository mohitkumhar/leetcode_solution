class Solution {
public:
    long long minimumCost(int cost1, int cost2, int costBoth, int need1,
                          int need2) {
        long long minCost = 0;

        long long costForBoth = min({costBoth, cost1 + cost2});

        long long both = min({need1, need2});

        minCost += both * costForBoth;

        need1 -= both;
        need2 -= both;

        long long costForNeed1 = min({cost1, costBoth});
        minCost += costForNeed1 * need1;

        long long costForNeed2 = min({cost2, costBoth});
        minCost += costForNeed2 * need2;

        return minCost;
    }
};