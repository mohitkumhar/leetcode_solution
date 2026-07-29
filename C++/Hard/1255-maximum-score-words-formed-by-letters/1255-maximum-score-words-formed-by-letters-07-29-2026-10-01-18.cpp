class Solution {
public:
    int bestScore = 0;

    void backtrack(int i, int currScore, vector<int>& freq, vector<int>& score,
                   vector<string>& words) {

        bestScore = max(bestScore, currScore);
        if (i >= words.size())
            return;

        // take
        int j = 0;
        vector<int> tempFreq = freq;
        int tempScore = 0;

        while (j < words[i].size()) {
            char ch = words[i][j];

            tempScore += score[ch - 'a'];
            tempFreq[ch - 'a']--;

            if (tempFreq[ch - 'a'] < 0)
                break;
            j++;
        }

        if (j == words[i].size()) {
            // take
            backtrack(i + 1, currScore + tempScore, tempFreq, score, words);
        }

        // skip
        backtrack(i + 1, currScore, freq, score, words);
    }

    int maxScoreWords(vector<string>& words, vector<char>& letters,
                      vector<int>& score) {

        vector<int> freq(26, 0);

        for (char letter : letters)
            freq[letter - 'a']++;

        backtrack(0, 0, freq, score, words);

        return bestScore;
    }
};