class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {

        int n = nums.size();

        int count = 0;
        int currSum = 0;

        map<int, int> prefixSum;
        prefixSum[0] = 1;

        for (int i = 0; i < n; i++) {
            currSum += nums[i];

            if (prefixSum.find(currSum - k) != prefixSum.end())
                count += prefixSum[currSum - k];

            prefixSum[currSum]++;
        }
        return count;
    }
};