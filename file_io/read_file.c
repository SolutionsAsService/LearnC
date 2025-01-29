#include <stdio.h>

// This program demonstrates how to read a file in C.
int main() {
    FILE *file = fopen("example.txt", "r");  // Open file in read mode
    if (file == NULL) {
        printf("Could not open the file.\n");
        return 1;  // Exit if the file couldn't be opened
    }

    char ch;
    while ((ch = fgetc(file)) != EOF) {  // Read the file character by character
        putchar(ch);  // Print each character to the console
    }

    fclose(file);  // Close the file after reading
    return 0;
}
