class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        
        unordered_set<int> hashSet(nums.begin(), nums.end());

        if (hashSet.size() == 1 && hashSet.find(0) != hashSet.end())
            return 0;

        int currXOR = 0;

        for (int num: nums)
            currXOR ^= num;

        if (currXOR != 0)
            return nums.size();
        return nums.size() - 1;
    }
};