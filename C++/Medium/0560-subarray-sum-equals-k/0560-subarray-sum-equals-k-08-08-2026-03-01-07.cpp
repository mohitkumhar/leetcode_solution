class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {

        int count = 0;
        int n = nums.size();

        map<int, int> prefixTable = {{0, 1}};

        int prefixSum = 0;

        for (int i = 0; i < n; i++) {
            prefixSum += nums[i];
            if (prefixTable.find(prefixSum - k) != prefixTable.end())
                count += prefixTable[prefixSum - k];

            prefixTable[prefixSum]++;
        }
        return count;
    }
};