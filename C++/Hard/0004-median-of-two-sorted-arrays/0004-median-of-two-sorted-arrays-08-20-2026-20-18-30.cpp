class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size();
        int len2 = nums2.size();

        int i = 0;
        int j = 0;

        vector<int> nums;

        while (i < len1 && j < len2) {

            if (nums1[i] < nums2[j]) {
                nums.push_back(nums1[i]);
                i++;
            } else {
                nums.push_back(nums2[j]);
                j++;
            }
        }

        while (i < len1) {
            nums.push_back(nums1[i]);
            i++;
        }
        while (j < len2) {
            nums.push_back(nums2[j]);
            j++;
        }

        if (nums.size() % 2 == 1)
            return nums[nums.size() / 2] / 1.0;

        return (nums[(nums.size() / 2) - 1] + nums[nums.size() / 2]) / 2.0;
    }
};