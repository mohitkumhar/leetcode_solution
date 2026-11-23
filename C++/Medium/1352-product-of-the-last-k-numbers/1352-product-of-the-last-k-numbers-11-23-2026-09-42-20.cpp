class ProductOfNumbers {
public:
    vector<int> prefixNums;

    ProductOfNumbers() { prefixNums.push_back(1); }

    void add(int num) {
        if (num == 0) {
            prefixNums.clear();
            prefixNums.push_back(1);
        } else {
            prefixNums.push_back(prefixNums.back() * num);
        }
    }

    int getProduct(int k) {
        int n = prefixNums.size();

        if (n <= k)
            return 0;
        return prefixNums[n - 1] / prefixNums[n - k - 1];
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */