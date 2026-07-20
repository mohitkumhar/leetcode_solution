class Solution {
public:
    int findHistogram(vector<int> heights) {
        int n = heights.size();

        vector<int> leftMiniVal;
        stack<int> stack;

        for (int i = 0; i < n; i++) {
            while (!stack.empty() && heights[stack.top()] >= heights[i])
                stack.pop();

            if (stack.empty())
                leftMiniVal.push_back(-1);
            else if (heights[stack.top()] < heights[i])
                leftMiniVal.push_back(stack.top());

            stack.push(i);
        }

        while (!stack.empty())
            stack.pop();

        vector<int> rightMiniVal;
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.empty() && heights[stack.top()] >= heights[i])
                stack.pop();

            if (stack.empty())
                rightMiniVal.push_back(n);
            else if (heights[stack.top()] < heights[i])
                rightMiniVal.push_back(stack.top());

            stack.push(i);
        }
        reverse(rightMiniVal.begin(), rightMiniVal.end());

        int maxArea = 0;

        for (int i = 0; i < n; i++) {
            int width = rightMiniVal[i] - leftMiniVal[i] - 1;
            maxArea = max(maxArea, heights[i] * width);
        }

        return maxArea;
    }

    int maximalRectangle(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int maxArea = 0;

        vector<int> heights(n);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1')
                    heights[j] += 1;
                else
                    heights[j] = 0;
            }
            int currArea = findHistogram(heights);
            maxArea = max(maxArea, currArea);
        }
        return maxArea;
    }
};