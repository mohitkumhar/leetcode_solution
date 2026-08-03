class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        map<int, int> numsDict;
        vector<int> result(2, 0);

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (numsDict.find(complement) != numsDict.end()) {
                result[0] = numsDict[complement];
                result[1] = i;
                break;
            }

            numsDict.insert({nums[i], i});
        }
        return result;
    }
};