class Solution {
public:
    int gcdOfOddEvenSums(int n) {
        int evenSum = 0;
        int oddSum = 0;

        for (int i = 0; i <= n * 2; i++) {
            if (i % 2 == 0) {
                evenSum += i;
            } else {
                oddSum += i;
            }
        }
        return __gcd(evenSum, oddSum);
    }
};