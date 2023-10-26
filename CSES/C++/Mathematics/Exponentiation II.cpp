#include <iostream>

const long long MOD = 1000000007;

long long fast_pow(long long a, long long b) {
    if (b == 0)
        return 1;
    
    long long res = fast_pow(a, b / 2) % MOD;
    res = (res * res) % MOD;
    
    if (b % 2 == 1)
        res = (res * a) % MOD;
    
    return res;
}

int main() {
    int n;
    std::cin >> n;

    for (int i = 0; i < n; ++i) {
        long long a, b, c;
        std::cin >> a >> b >> c;
        long long result = fast_pow(a, fast_pow(b, c) % MOD);
        std::cout << result << std::endl;
    }

    return 0;
}
