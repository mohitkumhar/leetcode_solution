class Solution {
public:
    int n = 0;

    int solve(int i, int j, string& str1, string& str2,
              vector<vector<int>>& memo) {
        if (i >= n || j >= n)
            return 0;
        if (memo[i][j] != -1)
            return memo[i][j];

        int ans = 0;

        if (str1[i] == str2[j])
            ans += (1 + solve(i + 1, j + 1, str1, str2, memo));
        else
            ans += max(solve(i + 1, j, str1, str2, memo),
                       solve(i, j + 1, str1, str2, memo));

        memo[i][j] = ans;
        return memo[i][j];
    }

    int longestPalindromeSubseq(string s) {
        string str1 = s;
        string str2 = str1;
        reverse(str2.begin(), str2.end());

        n = s.size();

        vector<vector<int>> memo(n, vector<int>(n, -1));

        return solve(0, 0, str1, str2, memo);
    }
};