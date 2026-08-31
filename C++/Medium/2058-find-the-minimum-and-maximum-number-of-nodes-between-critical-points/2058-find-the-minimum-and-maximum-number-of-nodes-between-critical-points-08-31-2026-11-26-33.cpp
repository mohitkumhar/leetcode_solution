/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {

        ListNode* prev = head;
        ListNode* curr = head->next;

        int index = 1;

        vector<int> criticalPoint;

        while (curr->next) {
            if (curr->val < prev->val && curr->val < curr->next->val)
                criticalPoint.push_back(index);

            else if (curr->val > prev->val && curr->val > curr->next->val)
                criticalPoint.push_back(index);

            index++;
            prev = curr;
            curr = curr->next;
        }

        if (criticalPoint.size() < 2)
            return {-1, -1};

        int maxVal = criticalPoint[criticalPoint.size() - 1] - criticalPoint[0];
        int minVal = INT_MAX;

        for (int i = 0; i < criticalPoint.size() - 1; i++) {
            int diff = criticalPoint[i + 1] - criticalPoint[i];
            minVal = min(minVal, diff);
        }

        return {minVal, maxVal};
    }
};