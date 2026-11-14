class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue<int> heap;
        for (int num : nums)
            heap.push(num);

        long long ans = 0;
        while (k--) {
            int currNum = heap.top();
            heap.pop();

            ans += currNum;

            long long currNumCeil = (currNum + 2) / 3;

            heap.push(currNumCeil);
        }
        return ans;
    }
};