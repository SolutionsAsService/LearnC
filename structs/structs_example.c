#include <stdio.h>

// Define a structure to store information about a person
struct Person {
    char name[50];
    int age;
};

int main() {
    // Initialize a structure variable
    struct Person person1 = {"John", 30};

    // Access structure members using dot operator
    printf("Name: %s\n", person1.name);  // Access name member
    printf("Age: %d\n", person1.age);    // Access age member

    return 0;
}
