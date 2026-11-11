#include <iostream>
#include <memory>

// RAII: a resource is tied to an object's lifetime.
struct Noisy {
    const char *name;
    explicit Noisy(const char *n) : name(n) { std::cout << "acquire " << name << '\n'; }
    ~Noisy() { std::cout << "release " << name << '\n'; }  // runs automatically
};

int main() {
    Noisy a("a");
    {
        auto b = std::make_unique<Noisy>("b");  // heap, but owned
        std::cout << "inner scope ends\n";
    }                                            // b released here, no free()
    std::cout << "main ends\n";
}                                                // a released here
