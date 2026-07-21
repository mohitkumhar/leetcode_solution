class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        vector<int> zero_count;
        int count = 0;
        int curr_ones = 0;

        for (char c : s) {
            if (c == '1') {
                curr_ones++;
                if (count > 0)
                    zero_count.push_back(count);
                count = 0;
            } else
                count++;
        }
        if (count > 0)
            zero_count.push_back(count);

        int max_ones = 0;
        if (zero_count.size() >= 2) {
            for (int i = 0; i < zero_count.size() - 1; i++) {
                if (zero_count[i] + zero_count[i + 1] > max_ones) {
                    max_ones = zero_count[i] + zero_count[i + 1];
                }
            }
        }
        return max_ones + curr_ones;
    }
};