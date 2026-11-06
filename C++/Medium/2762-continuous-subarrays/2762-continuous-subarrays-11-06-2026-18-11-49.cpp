class Solution {
public:
    long long continuousSubarrays(vector<int>& nums) {
        int n = nums.size();
        long long result = 0;

        int i = 0;
        int j = 0;

        deque<int> maxValues;
        deque<int> minValues;

        while (j < n) {
            while (!maxValues.empty() && nums[j] > maxValues.back()) {
                maxValues.pop_back();
            }
            maxValues.push_back(nums[j]);

            while (!minValues.empty() && nums[j] < minValues.back()) {
                minValues.pop_back();
            }
            minValues.push_back(nums[j]);

            while ((maxValues.front() - minValues.front()) > 2) {
                if (maxValues.front() == nums[i])
                    maxValues.pop_front();
                if (minValues.front() == nums[i])
                    minValues.pop_front();
                i++;
            }

            if (maxValues.front() - minValues.front() <= 2)
                result += (long long)(j - i + 1);
            j++;
        }
        return result;
    }
};