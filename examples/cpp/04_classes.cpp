#include <iostream>
#include <memory>
#include <vector>

class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;        // pure virtual: subclasses must define it
};

class Square : public Shape {
    double s;
public:
    explicit Square(double side) : s(side) {}
    double area() const override { return s * s; }
};

class Circle : public Shape {
    double r;
public:
    explicit Circle(double radius) : r(radius) {}
    double area() const override { return 3.14159 * r * r; }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Square>(2));
    shapes.push_back(std::make_unique<Circle>(1));
    for (const auto &s : shapes) std::cout << s->area() << '\n';  // dynamic dispatch
}
