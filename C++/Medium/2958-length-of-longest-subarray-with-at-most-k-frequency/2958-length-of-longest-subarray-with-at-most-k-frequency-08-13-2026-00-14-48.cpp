class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {

        int n = nums.size();

        map<long long, long long> map;
        int j = 0;
        int count = 0;

        for (int i = 0; i < n; i++) {
            while (j < n) {
                int value = nums[j];

                map[value]++;
                j++;

                if (map[value] > k) {
                    j--;
                    map[value]--;
                    break;
                }
            }
            count = max(count, j - i);
            map[nums[i]]--;
        }

        return count;
    }
};