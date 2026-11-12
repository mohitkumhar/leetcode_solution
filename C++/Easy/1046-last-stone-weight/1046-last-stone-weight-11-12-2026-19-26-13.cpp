class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {

        priority_queue<int> pq;

        for (int stone : stones)
            pq.push(stone);

        while (pq.size() > 1) {
            int firstHeavyStone = pq.top();
            pq.pop();

            int secondHeavyStone = pq.top();
            pq.pop();

            if (firstHeavyStone == secondHeavyStone)
                continue;
            else
                firstHeavyStone -= secondHeavyStone;
            pq.push(firstHeavyStone);
        }

        if (!pq.empty())
            return pq.top();
        return 0;
    }
};