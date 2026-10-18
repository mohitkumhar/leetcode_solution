class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        int maxKPos = -1;
        int minKPos = -1;
        int culpritIdx = -1;
        long long ans = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] < minK || nums[i] > maxK)
                culpritIdx = i;
            if (nums[i] == minK)
                minKPos = i;
            if (nums[i] == maxK)
                maxKPos = i;

            long long minValIdx = min(minKPos, maxKPos);
            long long tempAns = minValIdx - culpritIdx;

            ans += tempAns > 0 ? tempAns : 0;
        }
        return ans;
    }
};