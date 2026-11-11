#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> langs{"C", "C++", "Objective-C", "C#", "HolyC"};
    std::sort(langs.begin(), langs.end());

    std::map<std::string, int> born{{"C", 1972}, {"C++", 1985}, {"C#", 2000}};
    for (const auto &name : langs) {
        auto it = born.find(name);
        std::cout << name;
        if (it != born.end()) std::cout << " " << it->second;
        std::cout << '\n';
    }
}
