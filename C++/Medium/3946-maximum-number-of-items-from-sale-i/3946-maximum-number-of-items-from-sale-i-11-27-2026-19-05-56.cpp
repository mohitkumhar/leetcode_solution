class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n=items.size();
        vector<int>facs(n,0);
        for(int i=0;i<items.size();i++){
            for(int j=0;j<items.size();j++){
                if(i!=j && items[j][0]%items[i][0]==0)facs[i]++;
            }
        }
        vector<int>dp(budget+1,INT_MIN);dp[0]=0;
        for(int i=0;i<n;i++){
            int p=items[i][1];
            for(int c=budget;c>=p;c--){
                dp[c]=max(dp[c],dp[c-p]+facs[i]+1);
            }
            for(int c=p;c<=budget;c++){
                if(dp[c-p]!=INT_MIN)dp[c]=max(dp[c],dp[c-p]+1);
            }
        }
        return *max_element(dp.begin(),dp.end());
    }
};