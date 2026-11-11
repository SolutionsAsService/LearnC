#include <cmath>
#include <cstdio>

struct Point {
    double x, y;
    double length() const { return std::hypot(x, y); }  // a member function
};

int main() {
    Point p{3, 4};
    std::printf("%.1f\n", p.length());
}
