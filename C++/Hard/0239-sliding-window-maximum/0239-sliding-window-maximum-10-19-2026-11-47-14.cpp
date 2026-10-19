class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> q;
        vector<int> result;

        int n = nums.size();

        int i = 0;
        int j = 0;

        while (j < n) {
            while (!q.empty() && nums[j] > nums[q.back()])
                q.pop_back();
            q.push_back(j);

            if (j - i + 1 < k)
                j++;

            else if (j - i + 1 == k) {
                result.push_back(nums[q.front()]);

                if (nums[i] == nums[q.front()])
                    q.pop_front();

                i++;
                j++;
            }
        }
        return result;
    }
};