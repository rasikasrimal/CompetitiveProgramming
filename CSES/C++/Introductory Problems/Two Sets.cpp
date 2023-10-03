#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> finalSubsetWithSum(vector<int>& numbers, int total) {
    int n = numbers.size();
    vector<vector<bool>> dp(n + 1, vector<bool>(total + 1, false));

    // Initialize the DP table
    for (int i = 0; i <= n; i++) {
        dp[i][0] = true;
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= total; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j >= numbers[i - 1]) {
                dp[i][j] = dp[i][j] || dp[i - 1][j - numbers[i - 1]];
            }
        }
    }

    // Check if a valid subset exists
    if (!dp[n][total]) {
        return {};
    }

    // Backtrack to find the subsets
    vector<vector<int>> result;
    vector<int> currentSubset;
    int i = n, j = total;

    while (i > 0 && j > 0) {
        if (dp[i - 1][j]) {
            i--;
        } else {
            currentSubset.push_back(numbers[i - 1]);
            j -= numbers[i - 1];
            i--;
        }
    }

    result.push_back(currentSubset);
    return result;
}

int main() {
    int n;
    cin >> n;

    vector<int> mySet;
    for (int i = 1; i <= n; i++) {
        mySet.push_back(i);
    }

    int total = 0;
    for (int num : mySet) {
        total += num;
    }

    if (total % 2 == 1) {
        cout << "NO" << endl;
    } else {
        cout << "YES" << endl;
        vector<vector<int>> set1 = finalSubsetWithSum(mySet, total / 2);

        if (set1.empty()) {
            cout << "0" << endl;
        } else {
            cout << set1[0].size() << endl;
            for (int element : set1[0]) {
                cout << element << " ";
            }
            cout << endl;

            vector<int> set2;
            for (int element : mySet) {
                if (find(set1[0].begin(), set1[0].end(), element) == set1[0].end()) {
                    set2.push_back(element);
                }
            }

            cout << set2.size() << endl;
            for (int element : set2) {
                cout << element << " ";
            }
            cout << endl;
        }
    }

    return 0;
}
