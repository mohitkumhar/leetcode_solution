class Solution {
public:
    void backtrack(int i, vector<int>& children, int& result,
                   vector<int> cookies, int k) {
        if (i == cookies.size()) {
            result =
                min(result, *max_element(children.begin(), children.end()));
            return;
        }

        for (int j = 0; j < k; j++) {
            children[j] += cookies[i];
            backtrack(i + 1, children, result, cookies, k);
            children[j] -= cookies[i];

            if (children[j] == 0)
                break;
        }
    }

    int distributeCookies(vector<int>& cookies, int k) {
        int result = INT_MAX;
        vector<int> children(k, 0);

        backtrack(0, children, result, cookies, k);

        return result;
    }
};