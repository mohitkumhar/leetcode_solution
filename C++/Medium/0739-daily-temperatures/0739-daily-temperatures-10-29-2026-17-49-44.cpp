class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> st;
        vector<int> result;
        int n = temperatures.size();

        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && temperatures[st.top()] <= temperatures[i]) {
                st.pop();
            }
            if (st.empty()) {
                result.push_back(0);
            } else {
                result.push_back(st.top() - i);
            }
            st.push(i);
        }
        reverse(result.begin(), result.end());
        return result;
    }
};