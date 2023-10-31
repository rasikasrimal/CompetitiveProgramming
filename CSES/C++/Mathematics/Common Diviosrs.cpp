#include <iostream>
#include <vector>

int gcd(int a, int b) {
    while (b) {
        a = a % b;
        std::swap(a, b);
    }
    return a;
}

int find_max_gcd_pair(std::vector<int>& arr) {
    int n = arr.size();
    int max_gcd = -1;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int current_gcd = gcd(arr[i], arr[j]);
            if (current_gcd > max_gcd) {
                max_gcd = current_gcd;
            }
        }
    }

    return max_gcd;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    int result = find_max_gcd_pair(arr);
    std::cout << result << std::endl;

    return 0;
}
