class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        int n = nums.size();

        int i = 0;
        int j = 0;

        long long result = 0;
        int pairs = 0;
        unordered_map<int, int> freq;

        while (j < n) {
            pairs += freq[nums[j]];
            freq[nums[j]]++;

            while (pairs >= k) {
                result += n - j;
                freq[nums[i]]--;
                pairs -= freq[nums[i]];

                i++;
            }
            j++;
        }
        return result;
    }
};