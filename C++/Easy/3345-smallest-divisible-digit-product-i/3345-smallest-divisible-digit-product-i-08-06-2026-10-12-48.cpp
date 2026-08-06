class Solution {
public:
    int smallestNumber(int n, int t) {

        for (int i = n; i <= 100; i++) {
            string check = to_string(i);

            long long product = 1;
            for (char num : check)
                product *= (num - '0');

            if (product == 0 || product % t == 0)
                return i;
        }
        return -1;
    }
};