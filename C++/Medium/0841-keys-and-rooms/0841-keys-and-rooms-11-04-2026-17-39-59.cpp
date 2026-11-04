class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();

        queue<int> q;
        q.push(0);

        unordered_set<int> visited;
        visited.insert(0);

        while (!q.empty()) {
            int room = q.front();
            q.pop();

            for (int neiRooms : rooms[room]) {
                if (visited.find(neiRooms) == visited.end()) {
                    visited.insert(neiRooms);
                    q.push(neiRooms);
                }
            }
        }
        return visited.size() == n;
    }
};