#include <algorithm>

class Solution {
public:
    int maxDepth(string s) {
        stack<char> st;
        int ans = 0;

        for (char ch : s) {
            if (ch == '(')
                st.push(ch);
            else if (ch == ')')
                st.pop();

            ans = max({ans, static_cast<int>(st.size())});
        }
        return ans;
    }
};