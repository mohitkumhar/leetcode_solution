class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();

        if (n == 0) {
            return 0;
        }

        int currSeq = 1;
        int maxSeq = 1;
        unordered_set<int> elements(nums.begin(), nums.end());

        for (int ele : elements) {
            int tempAns = 1;
            if (elements.find(ele - 1) != elements.end())
                continue;

            else {
                while (elements.find(ele + 1) != elements.end()) {
                    tempAns++;
                    ele++;
                }
            }
            currSeq = tempAns;
            maxSeq = max(maxSeq, currSeq);
        }
        return maxSeq;
    }
};