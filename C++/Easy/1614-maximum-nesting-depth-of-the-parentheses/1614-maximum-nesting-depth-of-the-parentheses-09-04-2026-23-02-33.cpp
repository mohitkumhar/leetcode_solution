class Solution {
public:
    int maxDepth(string s) {
        stack<int> stack;
        int ans = 0;

        for (char ch : s) {
            if (ch == '(')
                stack.push(ch);
            else if (ch == ')')
                stack.pop();

            ans = max(ans, (int)stack.size());
        }
        return ans;
    }
};