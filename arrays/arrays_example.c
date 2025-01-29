#include <stdio.h>

// This program demonstrates arrays in C
int main() {
    int numbers[5] = {1, 2, 3, 4, 5};  // Declare an array of 5 integers

    // Loop through the array and print each element
    for (int i = 0; i < 5; i++) {
        printf("numbers[%d] = %d\n", i, numbers[i]);
    }

    return 0;
}
