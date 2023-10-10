#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int minimumCoins(int n, vector<int>& coins) {
    vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;
    
    for (int i = 1; i <= n; ++i) {
        for (int coin : coins) {
            if (i - coin >= 0) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    
    return dp[n] != INT_MAX ? dp[n] : -1;
}

int main() {
    int n, totalSum;
    cin >> n >> totalSum;
    
    vector<int> coins(n);
    for (int i = 0; i < n; ++i) {
        cin >> coins[i];
    }
    
    int result = minimumCoins(totalSum, coins);
    cout << result << endl;
    
    return 0;
}
