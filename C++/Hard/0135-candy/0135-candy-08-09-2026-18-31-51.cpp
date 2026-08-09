class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();

        vector<int> leftView(n, 1);
        vector<int> rightView(n, 1);

        for (int i = 1; i < n; i++)
            if (ratings[i - 1] < ratings[i])
                leftView[i] = leftView[i - 1] + 1;

        for (int i = n - 2; i >= 0; i--)
            if (ratings[i + 1] < ratings[i])
                rightView[i] = rightView[i + 1] + 1;

        int result = 0;

        for (int i = 0; i < n; i++)
            result += max(leftView[i], rightView[i]);

        return result;
    }
};