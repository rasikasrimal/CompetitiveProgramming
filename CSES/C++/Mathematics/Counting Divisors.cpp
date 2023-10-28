#include <iostream>
#include <vector>

int countDivisors(int num) {
    int divisors = 1;

    for (int i = 2; i * i <= num; ++i) {
        int exponent = 0;
        while (num % i == 0) {
            num /= i;
            exponent++;
        }
        divisors *= (exponent + 1);
    }

    if (num > 1) {
        divisors *= 2;
    }

    return divisors;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> numbers;

    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;
        int divisors = countDivisors(num);
        std::cout << divisors << std::endl;
    }

    return 0;
}
