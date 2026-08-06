class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        vector<int> mergedList;

        int i = 0;
        int j = 0;

        int m = nums1.size();
        int n = nums2.size();

        while (i < m && j < n) {
            if (nums1[i] < nums2[j]) {
                mergedList.push_back(nums1[i]);
                i++;
            } else {
                mergedList.push_back(nums2[j]);
                j++;
            }
        }

        while (i < m) {
            mergedList.push_back(nums1[i]);
            i++;
        }

        while (j < n) {
            mergedList.push_back(nums2[j]);
            j++;
        }

        n = mergedList.size();
        if (n % 2 == 1)
            return mergedList[n / 2];

        return (mergedList[(n / 2) - 1] + mergedList[(n / 2)]) / 2.0;
    }
};