class Solution {
public:
    // KMP Start
    void computeLPS(vector<int>& pattern, vector<int>& lps) {
        int M = pattern.size();
        int len = 0;
        lps[0] = 0;

        int i = 1;
        while (i < M) {
            if (pattern[i] == pattern[len]) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
    }

    bool search(vector<int>& pat, vector<int>& txt) {
        int N = txt.size();
        int M = pat.size();

        vector<int> lps(M, 0);
        computeLPS(pat, lps);

        int i = 0; // index for text
        int j = 0; // index for pattern

        while (i < N) {
            if (pat[j] == txt[i]) {
                i++;
                j++;
            }

            if (j == M) {
                return true; // pattern found , return true
            } else if (i < N && pat[j] != txt[i]) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return false;
    }
    // KMP End

    // Is vec1 a cyclic rotation of vec2 ,  then, vec1 occurs in vec2+vec2
    bool isRotation(vector<int>& vec1, vector<int>& vec2) {
        vector<int> txt = vec2;
        txt.insert(end(txt), begin(vec2), end(vec2)); // vec2 + vec2
        return search(vec1, txt);
    }

    int sortableIntegers(vector<int>& nums) {
        int n = nums.size();

        vector<int> sorted = nums;
        sort(begin(sorted), end(sorted));

        int result = 0;

        for (int k = 1; k <= n; k++) {
            if (n % k != 0)
                continue;

            bool isValid = true;

            for (int start = 0; start < n; start += k) {
                vector<int> vec1(begin(nums) + start, begin(nums) + start + k);
                vector<int> vec2(begin(sorted) + start,
                                 begin(sorted) + start + k);

                if (!isRotation(vec1, vec2)) {
                    isValid = false;
                    break;
                }
            }
            if (isValid)
                result += k;
        }
        return result;
    }
};