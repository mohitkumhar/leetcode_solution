class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char ch : s) {
            if (ch == '(' || ch == '[' || ch == '{') {
                st.push(ch);
            } else {
                if (st.empty())
                    return false;
                char popedValue = st.top();
                st.pop();

                if ((ch == ')' && popedValue != '(') ||
                    (ch == '}' && popedValue != '{') ||
                    (ch == ']' && popedValue != '['))
                    return false;
            }
        }
        if (st.empty())
            return true;
        return false;
    }
};