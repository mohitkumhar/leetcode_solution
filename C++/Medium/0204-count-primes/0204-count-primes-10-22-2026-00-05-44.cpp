class Solution {
public:
    int countPrimes(int n) {
        if (n < 2)
            return 0;

        vector<bool> isPrime(n, true);

        isPrime[0] = false;
        isPrime[1] = false;

        int i = 2;

        while (i * i < n) {
            if (isPrime[i]) {
                int j = i * i;

                while (j < n) {
                    isPrime[j] = false;
                    j += i;
                }
            }
            i++;
        }

        return count(isPrime.begin(), isPrime.end(), true);
    }
};