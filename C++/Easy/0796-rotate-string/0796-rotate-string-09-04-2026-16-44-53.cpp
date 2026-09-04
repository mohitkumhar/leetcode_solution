class Solution {
public:
    bool rotateString(string s, string goal) {
        return s.size() == goal.size() && (goal + goal).find(s) != string::npos;
    }
};