#include <stdio.h>

int add(int a, int b);         /* declaration: the promise */

static int factorial(int n) {  /* static: visible only in this file */
    return n <= 1 ? 1 : n * factorial(n - 1);
}

int main(void) {
    printf("The sum is: %d\n", add(10, 20));
    printf("5! = %d\n", factorial(5));
    return 0;
}

int add(int a, int b) {        /* definition: the body */
    return a + b;
}
