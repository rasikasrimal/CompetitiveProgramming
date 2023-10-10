#include <iostream>

int main() {
    long long n;
    std::cin >> n;

    if (n % 2 == 0) {
        std::cout << "YES" << std::endl;
        std::cout << n / 2 << std::endl;
        for (long long i = 1; i <= n / 2; ++i) {
            std::cout << i << " ";
        }
        std::cout << std::endl;

        std::cout << n / 2 - 1 << std::endl;
        for (long long i = n / 2 + 1; i <= n; ++i) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    } else {
        std::cout << "NO" << std::endl;
    }

    return 0;
}
