#include <algorithm>
#include <iostream>
#include <string>

int main() {
    std::string s = "pointer";
    std::reverse(s.begin(), s.end());
    std::cout << s << '\n';
}
