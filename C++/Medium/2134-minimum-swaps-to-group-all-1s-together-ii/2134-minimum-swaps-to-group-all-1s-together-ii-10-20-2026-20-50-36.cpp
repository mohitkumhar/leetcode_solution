class Solution {
public:
    int minSwaps(vector<int>& nums) {

        int i = 0;
        int j = 0;

        int k = count(nums.begin(), nums.end(), 1);

        vector<int> temp = nums;
        nums.insert(nums.end(), temp.begin(), temp.end());

        int n = nums.size();

        int currOnes = 0;
        int ans = INT_MAX;

        if (k == 0 || k == n)
            return 0;

        while (j < n) {
            if (nums[j] == 1)
                currOnes++;

            if (j - i + 1 < k)
                j++;

            else if (j - i + 1 == k) {
                ans = min(ans, k - currOnes);

                if (nums[i] == 1)
                    currOnes--;
                i++;
                j++;
            }
        }
        return ans;
    }
};