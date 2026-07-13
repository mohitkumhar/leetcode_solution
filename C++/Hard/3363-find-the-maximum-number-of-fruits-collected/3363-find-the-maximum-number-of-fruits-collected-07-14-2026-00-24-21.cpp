class Solution {
public:
    int find_child_1_score(vector<vector<int>>& fruits) {
        int count = 0;
        for (int i = 0; i < fruits.size(); i++) {
            count += fruits[i][i];
        }
        return count;
    }

    int find_child_2_score(int i, int j, int moves, vector<vector<int>>& fruits,
                           vector<vector<int>>& memo) {
        int n = fruits.size();
        if (i >= n || j >= n || j < 0) {
            return 0;
        } else if (moves >= n - 1) {
            return 0;
        } else if (i == j || i > j) {
            return 0;
        } else if (memo[i][j] != -1) {
            return memo[i][j];
        }

        int bottom_left =
            fruits[i][j] +
            find_child_2_score(i + 1, j - 1, moves + 1, fruits, memo);
        int bottom_down = fruits[i][j] +
                          find_child_2_score(i + 1, j, moves + 1, fruits, memo);
        int bottom_right =
            fruits[i][j] +
            find_child_2_score(i + 1, j + 1, moves + 1, fruits, memo);

        memo[i][j] = max({bottom_left, bottom_down, bottom_right});
        return memo[i][j];
    }

    int find_child_3_score(int i, int j, int moves, vector<vector<int>>& fruits,
                           vector<vector<int>>& memo) {
        int n = fruits.size();
        if (i >= n || j >= n || i < 0) {
            return 0;
        } else if (moves >= n - 1) {
            return 0;
        } else if (i == j || i < j) {
            return 0;
        } else if (memo[i][j] != -1) {
            return memo[i][j];
        }

        int up_right =
            fruits[i][j] +
            find_child_3_score(i - 1, j + 1, moves + 1, fruits, memo);
        int right = fruits[i][j] +
                    find_child_3_score(i, j + 1, moves + 1, fruits, memo);
        int bottom_right =
            fruits[i][j] +
            find_child_3_score(i + 1, j + 1, moves + 1, fruits, memo);

        memo[i][j] = max({up_right, right, bottom_right});
        return memo[i][j];
    }

    int maxCollectedFruits(vector<vector<int>>& fruits) {
        int n = fruits.size();

        vector<vector<int>> memo(n, vector<int>(n, -1));

        int child_1_score = find_child_1_score(fruits);
        int child_2_score = find_child_2_score(0, n - 1, 0, fruits, memo);
        int child_3_score = find_child_3_score(n - 1, 0, 0, fruits, memo);

        return child_1_score + child_2_score + child_3_score;
    }
};