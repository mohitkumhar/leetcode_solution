class Solution {
public:
    int helper(int i, int count, int k, vector<int>& subArray,
               vector<vector<int>>& memo) {
        if (count == 0)
            return 0;
        if (i >= subArray.size())
            return INT_MIN;

        if (memo[i][count] != -1)
            return memo[i][count];

        int take = subArray[i] + helper(i + k, count - 1, k, subArray, memo);
        int skip = helper(i + 1, count, k, subArray, memo);

        return memo[i][count] = max(take, skip);
    }

    void solve(int i, int count, int k, vector<int>& subArray,
               vector<int>& result, vector<vector<int>>& memo) {
        if (count == 0)
            return;
        if (i >= subArray.size())
            return;

        int takeFromi =
            subArray[i] + helper(i + k, count - 1, k, subArray, memo);
        int skipFromi = helper(i + 1, count, k, subArray, memo);

        if (takeFromi >= skipFromi) {
            result.push_back(i);
            solve(i + k, count - 1, k, subArray, result, memo);
        } else {
            solve(i + 1, count, k, subArray, result, memo);
        }
    }

    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        vector<int> subArray;

        int i = 0;
        int j = 0;
        int currSum = 0;

        while (j < nums.size()) {
            currSum += nums[j];

            if (j - i + 1 == k) {
                subArray.push_back(currSum);
                currSum -= nums[i];
                i++;
            }
            j++;
        }

        vector<int> result;
        int n = subArray.size();
        vector<vector<int>> memo(n + 1, vector<int>(4, -1));

        solve(0, 3, k, subArray, result, memo);

        return result;
    }
};