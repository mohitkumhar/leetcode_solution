class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int> pq;

        for (int pile : piles)
            pq.push(pile);

        for (int i = 0; i < k; i++) {
            int currPile = pq.top();
            pq.pop();

            currPile = (currPile + 1) / 2;

            pq.push(currPile);
        }

        int count = 0;
        while (!pq.empty()) {
            count += pq.top();
            pq.pop();
        }

        return count;
    }
};