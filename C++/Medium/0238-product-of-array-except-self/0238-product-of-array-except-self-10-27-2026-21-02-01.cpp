class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();

        vector<int> leftMulti;
        long long currLeftVal = 1;

        for (int num : nums) {
            currLeftVal *= num;
            leftMulti.push_back(currLeftVal);
        }

        vector<int> rightMulti;
        long long currRightVal = 1;

        for (int i = n - 1; i >= 0; i--) {
            currRightVal *= nums[i];
            rightMulti.push_back(currRightVal);
        }

        reverse(rightMulti.begin(), rightMulti.end());
        int leftVal = 0;
        int rightVal = 0;

        vector<int> result;

        for (int i = 0; i < n; i++) {
            if (i > 0)
                leftVal = leftMulti[i - 1];
            else
                leftVal = 1;

            if (i < n - 1)
                rightVal = rightMulti[i + 1];
            else
                rightVal = 1;

            result.push_back(leftVal * rightVal);
        }
        return result;
    }
};