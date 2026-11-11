#include <iostream>

void swap(int &a, int &b) { int t = a; a = b; b = t; }  // references: no & at the call

int main() {
    int x = 1, y = 2;
    swap(x, y);
    std::cout << "x=" << x << " y=" << y << '\n';
}
