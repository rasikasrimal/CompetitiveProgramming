#include <iostream>
#include <vector>
#include <set>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
        std::cin >> numbers[i];
    }

    std::set<int> distinctNumbers(numbers.begin(), numbers.end());
    int distinct = distinctNumbers.size();

    std::cout << distinct << std::endl;

    return 0;
}
