#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int countWaysToConstructSum(int n) {
    vector<int> ways(n + 1, 0);
    ways[0] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= 6; ++j) {
            if (i >= j) {
                ways[i] = (ways[i] + ways[i - j]) % MOD;
            }
        }
    }

    return ways[n];
}

int main() {
    int n;
    cin >> n;
    int result = countWaysToConstructSum(n);
    cout << result << endl;
    return 0;
}
