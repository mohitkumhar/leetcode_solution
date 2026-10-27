class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0;
        int prefixSum = 0;
        unordered_map<int, int> prefixCount;

        prefixCount[0] = 1;

        for (int num : nums) {
            prefixSum += num;

            count += prefixCount[prefixSum - k];

            prefixCount[prefixSum]++;
        }
        return count;
    }
};