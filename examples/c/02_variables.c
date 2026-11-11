#include <stdio.h>

int main(void) {
    int age = 25;          /* whole number */
    double height = 5.9;   /* floating point */
    char grade = 'A';      /* one byte, a character code */

    printf("Age: %d\n", age);           /* %d: int */
    printf("Height: %.2f\n", height);   /* %.2f: two decimals */
    printf("Grade: %c (code %d)\n", grade, grade);
    printf("sizeof: int %zu, double %zu, char %zu bytes\n",
           sizeof age, sizeof height, sizeof grade);
    return 0;
}
