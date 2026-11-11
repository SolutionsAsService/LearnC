#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> v(10);
    std::iota(v.begin(), v.end(), 1);                 // 1, 2, ... 10
    std::cout << std::accumulate(v.begin(), v.end(), 0) << '\n';
}
