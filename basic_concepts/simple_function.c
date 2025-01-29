#include <stdio.h>

// Function declaration
int addNumbers(int a, int b);

int main() {
    int result = addNumbers(10, 20);  // Calling the function with arguments 10 and 20
    printf("The sum is: %d\n", result);  // Print the result
    return 0;
}

// Function definition
int addNumbers(int a, int b) {
    return a + b;  // Returns the sum of a and b
}
