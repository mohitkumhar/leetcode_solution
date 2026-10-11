class Solution {
public:
    int minNumberOperations(vector<int>& target) {
        int n = target.size();

        long long result = 0;

        int prev = 0;
        int curr = 0;

        for (int i = 0; i < n; i++) {
            curr = target[i];

            if (prev < 0 && curr > 0 || prev > 0 && curr < 0)
                result += abs(curr);
            else if (curr > prev)
                result += abs(prev - curr);
            prev = curr;
        }
        return result;
    }
};