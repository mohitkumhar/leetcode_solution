class Solution {
public:
    long long findCountSmallest(long long midProd, vector<int>& nums1,
                                vector<int>& nums2) {
        int n = nums2.size();
        long long productsCount = 0;

        for (int i = 0; i < nums1.size(); i++) {
            if (nums1[i] > 0) {
                // prod will be +ve

                int l = 0;
                int r = n - 1;
                int m = -1;

                while (l <= r) {
                    int mid = l + (r - l) / 2;
                    long long prod = 1LL * nums1[i] * nums2[mid];

                    if (prod <= midProd) {
                        m = mid;
                        l = mid + 1;
                    } else
                        r = mid - 1;
                }
                productsCount += (m + 1);

            } else {
                // prod will be -ve

                int l = 0;
                int r = n - 1;
                int m = n;

                while (l <= r) {
                    int mid = l + (r - l) / 2;
                    long long prod = 1LL * nums1[i] * nums2[mid];

                    if (prod <= midProd) {
                        m = mid;
                        r = mid - 1;
                    } else
                        l = mid + 1;
                }
                productsCount += (n - m);
            }
        }
        return productsCount;
    }

    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2,
                                 long long k) {

        long long result = 0;

        long long left = -1e10;
        long long right = 1e10;

        while (left <= right) {
            long long mid = left + (right - left) / 2;

            long long countSmallest = findCountSmallest(mid, nums1, nums2);

            if (countSmallest >= k) {
                result = mid;
                right = mid - 1;
            } else
                left = mid + 1;
        }
        return result;
    }
};