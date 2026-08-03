class Solution {
public:
    void sortColors(vector<int>& nums) {

        int zeros = 0;
        int ones = 0;
        int twos = 0;

        for (int num : nums) {
            if (num == 0)
                zeros++;
            else if (num == 1)
                ones++;
            else
                twos++;
        }

        int k = 0;
        while (zeros-- != 0)
            nums[k++] = 0;

        while (ones-- != 0)
            nums[k++] = 1;

        while (twos-- != 0)
            nums[k++] = 2;

        for (int i = 0; i < nums.size(); i++)
            cout << nums[i] << " ";
    }
};