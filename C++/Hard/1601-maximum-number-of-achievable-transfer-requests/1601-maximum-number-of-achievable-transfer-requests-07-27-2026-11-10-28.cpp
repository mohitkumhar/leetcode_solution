class Solution {
public:
    void backtrack(int i, int count, int& result, vector<int>& resultant,
                   vector<vector<int>>& requests) {
        if (i == requests.size()) {
            bool isZero = true;
            for (int num : resultant)
                if (num != 0) {
                    isZero = false;
                    break;
                }
            if (isZero == true)
                result = max(result, count);
            return;
        }

        // take
        resultant[requests[i][0]]--;
        resultant[requests[i][1]]++;

        backtrack(i + 1, count + 1, result, resultant, requests);

        resultant[requests[i][0]]++;
        resultant[requests[i][1]]--;

        // skip
        backtrack(i + 1, count, result, resultant, requests);
    }

    int maximumRequests(int n, vector<vector<int>>& requests) {
        int result = 0;
        vector<int> resultant(n, 0);

        backtrack(0, 0, result, resultant, requests);

        return result;
    }
};