#include <stdio.h>

// This program demonstrates variables and basic data types in C
int main() {
    int age = 25;               // Integer data type
    float height = 5.9;         // Floating-point data type
    char grade = 'A';           // Character data type

    // Printing the values of variables
    printf("Age: %d\n", age);          // %d is used for integers
    printf("Height: %.2f\n", height);  // %.2f formats the float to 2 decimal places
    printf("Grade: %c\n", grade);      // %c is used for characters

    return 0;
}
