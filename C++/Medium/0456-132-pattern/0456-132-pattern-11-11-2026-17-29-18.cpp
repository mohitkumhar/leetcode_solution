class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        stack<int> st;
        int num_3 = INT_MIN;

        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] < num_3) {
                return true;
            }

            while (!st.empty() && nums[i] > st.top()) {
                num_3 = st.top();
                st.pop();
            }
            st.push(nums[i]);
        }
        return false;
    }
};