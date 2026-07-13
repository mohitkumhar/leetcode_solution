class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int> q{1, 2, 3, 4, 5, 6, 7, 8, 9};

        for (int i = 0; i < (int)q.size(); i++) {
            int d = q[i] % 10;
            if (d < 9) {
                q.push_back(q[i] * 10 + d + 1);
            }
        }

        vector<int> result{};
        for (int num : q) {
            if (num >= low && num <= high) {
                result.push_back(num);
            }
        }
        return result;
    }
};