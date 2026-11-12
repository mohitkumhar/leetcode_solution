class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int n = nums.size();

        int currIncCount = 0;
        int currDecCount = 0;

        int incCount = 0;
        int decCount = 0;

        int prev = INT_MIN;

        for (int num : nums) {
            if (prev == INT_MIN) {
                prev = num;
                continue;
            }

            if (num > prev) {
                currIncCount += 1;
            } else {
                currIncCount = 0;
            }

            if (num < prev) {
                currDecCount += 1;
            } else {
                currDecCount = 0;
            }

            incCount = max({incCount, currIncCount});
            decCount = max({decCount, currDecCount});

            prev = num;
        }
        int ans = max({incCount, decCount});

        return ans == 0 ? 1 : ans + 1;
    }
};