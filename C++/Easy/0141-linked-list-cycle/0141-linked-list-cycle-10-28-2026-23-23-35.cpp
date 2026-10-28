/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode* curr = head;
        unordered_set<ListNode*> seen;

        while (curr != NULL) {
            if (seen.find(curr) != seen.end()) {
                return true;
            }
            seen.insert(curr);
            curr = curr->next;
        }
        return false;
    }
};