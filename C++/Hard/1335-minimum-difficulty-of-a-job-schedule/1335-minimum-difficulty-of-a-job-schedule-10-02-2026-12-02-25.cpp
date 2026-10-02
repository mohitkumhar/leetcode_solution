class Solution {
public:
    int solve(int idx, int day, vector<int>& jobDifficulty,
              vector<vector<int>>& memo) {
        if (day == 1)
            return *max_element(jobDifficulty.begin() + idx,
                                jobDifficulty.end());

        if (memo[idx][day] != -1)
            return memo[idx][day];

        int maxDay = INT_MIN;
        int finalResult = INT_MAX;

        for (int i = idx; i <= jobDifficulty.size() - day; i++) {
            maxDay = max(maxDay, jobDifficulty[i]);
            int result = maxDay + solve(i + 1, day - 1, jobDifficulty, memo);
            finalResult = min(finalResult, result);
        }

        return memo[idx][day] = finalResult;
    }

    int minDifficulty(vector<int>& jobDifficulty, int d) {
        if (jobDifficulty.size() < d)
            return -1;

        vector<vector<int>> memo(jobDifficulty.size(), vector<int>(d + 1, -1));
        return solve(0, d, jobDifficulty, memo);
    }
};