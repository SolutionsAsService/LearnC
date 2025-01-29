#include <stdio.h>

// This program demonstrates pointers in C
int main() {
    int num = 10;
    int *ptr = &num;  // Pointer to store the address of num

    // Print the value of num and its address
    printf("Value of num: %d\n", num);  // Direct access to num
    printf("Address of num: %p\n", &num);  // Address of num using & operator
    printf("Pointer ptr holds address: %p\n", ptr);  // Value of ptr is the address of num
    printf("Value pointed to by ptr: %d\n", *ptr);  // Dereferencing pointer to access value of num

    return 0;
}
