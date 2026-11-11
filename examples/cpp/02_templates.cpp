#include <iostream>
#include <string>

// One definition, many types: the compiler writes each version.
template <typename T>
T largest(T a, T b) { return a > b ? a : b; }

int main() {
    std::cout << largest(3, 7) << '\n';
    std::cout << largest(2.5, 1.5) << '\n';
    std::cout << largest(std::string("C"), std::string("C++")) << '\n';
}
