#include <iostream>
#include <vector>
#include <cmath>

int main() {
    int n;
    std::cin >> n;
    std::vector<long long> numbers;

    for (int i = 0; i < n; ++i) {
        int a, b;
        std::cin >> a >> b;
        long long result = std::pow(a, b);
        result = result % 1000000007;
        numbers.push_back(result);
    }

    for (long long number : numbers) {
        std::cout << number << std::endl;
    }

    return 0;
}
