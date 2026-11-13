class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {

        unordered_map<char, int> map;

        for (char task : tasks)
            map[task]++;

        priority_queue<int> pq;

        for (auto& it : map)
            pq.push(it.second);

        int time = 0;
        while (!pq.empty()) {
            vector<int> temp;

            for (int i = 0; i <= n; i++) {
                if (!pq.empty()) {
                    temp.push_back(pq.top() - 1);
                    pq.pop();
                }
            }

            for (int freq : temp) {
                if (freq > 0)
                    pq.push(freq);
            }

            if (pq.empty())
                time += temp.size();
            else
                time += n + 1;
        }
        return time;
    }
};