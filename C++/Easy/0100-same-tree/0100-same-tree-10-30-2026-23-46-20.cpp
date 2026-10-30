/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
    void solve(TreeNode* node, vector<int>& val) {
        if (!node) {
            val.push_back(INT_MIN);
            return;
        }
        solve(node->left, val);
        solve(node->right, val);

        val.push_back(node->val);
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        vector<int> a, b;

        solve(p, a);
        solve(q, b);

        return a == b;
    }
};