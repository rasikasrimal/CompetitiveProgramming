#include <iostream>
#include <vector>
#include <climits>
#include <cmath>
using namespace std;

int appleDivision(int n, vector<int>& p) {
    int totalSum = 0;
    for (int i = 0; i < n; i++) {
        totalSum += p[i];
    }
    
    int minDiff = INT_MAX;
    for (int i = 1; i < (1 << n); i++) {
        int currSum = 0;
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                currSum += p[j];
            }
        }
        minDiff = min(minDiff, abs(totalSum - 2 * currSum));
    }
    
    return minDiff;
}

int main() {
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }
    
    int result = appleDivision(n, p);
    cout << result << endl;
    return 0;
}
