class Solution {
public:
    int countPair(int left, int mid, int right, vector<int>& nums) {
        int i = left;
        int j = mid + 1;

        int count = 0;

        for (int i = left; i < mid + 1; i++) {
            while (j <= right && nums[i] > 2LL * nums[j])
                j++;
            count = count + (j - (mid + 1));
        }
        return count;
    }

    int merge(int left, int mid, int right, vector<int>& nums) {

        vector<int> nums1(nums.begin() + left, nums.begin() + mid + 1);
        vector<int> nums2(nums.begin() + mid + 1, nums.begin() + right + 1);

        int len1 = nums1.size();
        int len2 = nums2.size();

        int i = 0;
        int j = 0;

        int k = left;
        int count = 0;

        while (i < len1 && j < len2) {
            if (nums1[i] > nums2[j]) {
                nums[left] = nums2[j];
                j++;
                count += len1 - i;
            } else {
                nums[left] = nums1[i];
                i++;
            }
            left++;
        }

        while (i < len1) {
            nums[left] = nums1[i];
            i++;
            left++;
        }
        while (j < len2) {
            nums[left] = nums2[j];
            j++;
            left++;
        }
        return count;
    }

    int mergeSort(int left, int right, vector<int>& nums) {

        if (left >= right)
            return 0;

        int count = 0;

        int mid = left + (right - left) / 2;

        count += mergeSort(left, mid, nums);
        count += mergeSort(mid + 1, right, nums);

        count += countPair(left, mid, right, nums);

        merge(left, mid, right, nums);

        return count;
    }

    int reversePairs(vector<int>& nums) {
        int n = nums.size();

        int count = mergeSort(0, n - 1, nums);

        return count;
    }
};