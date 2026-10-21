class Solution {
public:
    int helper(vector<int> prefixSum, int l, int r) {
        int n = prefixSum.size();
        int result = 0;
        int leftSubSum = 0;

        for (int rEnd = l + r - 1; rEnd < n; rEnd++) {
            int lEnd = rEnd - r;
            int lStart = lEnd - l;

            int leftBlockSum =
                prefixSum[lEnd] - (lStart < 0 ? 0 : prefixSum[lStart]);
            int rightBlockSum = prefixSum[rEnd] - prefixSum[lEnd];

            leftSubSum = max(leftSubSum, leftBlockSum);

            result = max(result, leftSubSum + rightBlockSum);
        }
        return result;
    }

    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
        int n = nums.size();
        vector<int> prefixSum(n, 0);
        prefixSum[0] = nums[0];

        for (int i = 1; i < n; i++) {
            prefixSum[i] = prefixSum[i - 1] + nums[i];
        }

        return max(helper(prefixSum, firstLen, secondLen),
                   helper(prefixSum, secondLen, firstLen));
    }
};