class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        vector<int> result;
        int depth = 0;

        for (char ch : seq) {
            if (ch == '(') {
                result.push_back(depth % 2);
                depth++;
            } else {
                depth--;
                result.push_back(depth % 2);
            }
        }

        return result;
    }
};