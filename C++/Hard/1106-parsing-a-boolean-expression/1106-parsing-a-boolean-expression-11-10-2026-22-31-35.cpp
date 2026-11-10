class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<char> st;

        for (char exp : expression) {
            if (exp == ',')
                continue;

            else if (exp != ')') {
                st.push(exp);
            }

            else {
                vector<int> values;

                while (st.top() != '(') {
                    values.push_back(st.top());
                    st.pop();
                }

                st.pop(); // '('

                char op = st.top();
                st.pop();

                bool result = false;

                if (op == '|') {
                    result = false;

                    for (char val : values) {
                        if (val == 't') {
                            result = true;
                            break;
                        }
                    }
                }

                else if (op == '&') {
                    result = true;

                    for (char val : values) {
                        if (val == 'f') {
                            result = false;
                            break;
                        }
                    }
                }

                else {
                    result = values[0] == 'f' ? true : false;
                }

                if (result == true)
                    st.push('t');
                else
                    st.push('f');
            }
        }

        return st.top() == 't';
    }
};