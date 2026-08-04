class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {

        int n = nums.size();

        vector<int> posValues;
        vector<int> negValues;

        for (int num : nums) {
            if (num < 0)
                negValues.push_back(num);
            else
                posValues.push_back(num);
        }

        int k = 0;
        int i = 0;

        while (k < n) {
            nums[k++] = posValues[i];
            nums[k++] = negValues[i++];
        }

        return nums;
    }
};