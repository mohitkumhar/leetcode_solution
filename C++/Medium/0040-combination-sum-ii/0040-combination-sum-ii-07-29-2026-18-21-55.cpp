class Solution {
public:
    void backtrack(int i, int currSum, vector<int>& currComb,
                   vector<vector<int>>& result, vector<int>& candidates,
                   int target) {
        if (currSum == target) {
            result.push_back(currComb);
            return;
        }
        if (i >= candidates.size() || currSum > target) {
            return;
        }

        for (int j = i; j < candidates.size(); j++) {
            if (j > i && candidates[j] == candidates[j - 1])
                continue;
            currComb.push_back(candidates[j]);
            currSum += candidates[j];
            backtrack(j + 1, currSum, currComb, result, candidates, target);
            currSum -= candidates[j];
            currComb.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());

        vector<vector<int>> result;
        vector<int> currComb;

        backtrack(0, 0, currComb, result, candidates, target);

        return result;
    }
};