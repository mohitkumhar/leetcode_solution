class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> pos_ele;
        vector<int> neg_ele;
        vector<int> result(n);

        for (int num : nums) {
            if (num >= 0)
                pos_ele.push_back(num);
            else
                neg_ele.push_back(num);
        }

        int i = 0;
        int j = 0;
        int k = 0;

        while (k < n) {
            result[k++] = pos_ele[i++];
            result[k++] = neg_ele[j++];
        }
        return result;
    }
};