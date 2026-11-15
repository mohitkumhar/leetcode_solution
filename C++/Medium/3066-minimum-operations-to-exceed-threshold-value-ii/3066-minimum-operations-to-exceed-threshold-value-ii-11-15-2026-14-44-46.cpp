class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        priority_queue<long long, vector<long long>, greater<long long>> heap;

        for (int num : nums) {
            heap.push(num);
        }

        int opn = 0;

        while (heap.size() > 1) {
            long long small_1 = heap.top();
            heap.pop();
            long long small_2 = heap.top();
            heap.pop();
            if (small_1 >= k)
                return opn;

            long long newNum = small_1 * 2 + small_2;

            heap.push(newNum);
            opn++;
        }
        return opn;
    }
};