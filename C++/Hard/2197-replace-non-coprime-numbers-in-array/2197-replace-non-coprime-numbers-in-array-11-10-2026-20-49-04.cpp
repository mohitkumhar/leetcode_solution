class Solution {
public:
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        stack<int> st;

        for (int num : nums) {
            while (!st.empty() && gcd(st.top(), num) > 1) {
                int num1 = num;
                int num2 = st.top();
                st.pop();

                num = lcm(num1, num2);
            }
            st.push(num);
        }

        vector<int> ans;

        while (!st.empty()) {
            ans.push_back(st.top());
            st.pop();
        }
        reverse(ans.begin(), ans.end());

        return ans;
    }
};