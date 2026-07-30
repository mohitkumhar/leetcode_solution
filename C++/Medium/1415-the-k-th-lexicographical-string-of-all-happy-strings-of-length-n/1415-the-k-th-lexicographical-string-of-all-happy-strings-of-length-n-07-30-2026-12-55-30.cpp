class Solution {
public:
    void backtrack(int i, vector<char>& currComb, char prev,
                   vector<string>& result, vector<char>& s, int n) {

        if (currComb.size() == n) {
            string sentence;
            for (char c : currComb)
                sentence += c;
            result.push_back(sentence);
            return;
        }

        for (int j = 0; j < 3; j++) {
            if (prev == '#' || s[j] != prev) {
                currComb.push_back(s[j]);
                char temp = prev;
                prev = s[j];

                backtrack(j + 1, currComb, prev, result, s, n);

                prev = temp;
                currComb.pop_back();
            }
        }
    }

    string getHappyString(int n, int k) {
        vector<char> s = {'a', 'b', 'c'};

        vector<string> result;
        char prev = '#';
        vector<char> currComb;

        backtrack(0, currComb, prev, result, s, n);

        if ((k - 1) >= result.size())
            return "";
        return result[k - 1];
    }
};