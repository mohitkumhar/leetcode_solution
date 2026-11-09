class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();

        stack<int> st;
        int count = 0;

        for (int num : nums) {
            while (!st.empty() && st.top() > num) {
                st.pop();
            }

            if (num == 0)
                continue;

            if (st.empty() || st.top() < num) {
                st.push(num);
                count++;
            }
        }
        return count;
    }
};