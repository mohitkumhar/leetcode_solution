class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter,
                      int x1, int y1, int x2, int y2) {

        // Find the closest point of rectangle to circle center
        int closestX = max(x1, min(xCenter, x2));
        int closestY = max(y1, min(yCenter, y2));

        // Calculate squared distance
        int dx = xCenter - closestX;
        int dy = yCenter - closestY;

        // Check if closest point is inside/on circle
        return dx * dx + dy * dy <= radius * radius;
    }
};