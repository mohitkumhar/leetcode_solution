class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();

        int i = 0;
        int k = 0;

        while (i < n && k < n) {
            if (nums[i] == nums[k])
                i++;
            else {
                k++;
                nums[k] = nums[i];
            }
        }
        return k + 1;
    }
};
