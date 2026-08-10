class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> result;

        sort(nums.begin(), nums.end());

        for (int k = 0; k < n - 2; k++) {
            if (k > 0 && nums[k] == nums[k - 1])
                continue;

            int low = k + 1;
            int high = n - 1;

            while (low < high) {
                int currSum = nums[k] + nums[low] + nums[high];

                if (currSum == 0) {
                    result.push_back({nums[k], nums[low], nums[high]});

                    while (low < high && nums[low] == nums[low + 1])
                        low++;
                    while (low < high && nums[high] == nums[high - 1])
                        high--;

                    low++;
                    high--;
                }

                else if (currSum > 0)
                    high--;
                else
                    low++;
            }
        }
        return result;
    }
};