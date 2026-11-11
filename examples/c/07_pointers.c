#include <stdio.h>

static void swap(int *a, int *b) {  /* receives addresses, not copies */
    int t = *a;
    *a = *b;
    *b = t;
}

int main(void) {
    int num = 10;
    int *ptr = &num;               /* ptr holds the address of num */

    printf("Value of num: %d\n", num);
    printf("ptr == &num: %s\n", ptr == &num ? "yes" : "no");
    *ptr = 42;                     /* write through the pointer */
    printf("After *ptr = 42, num is %d\n", num);

    int x = 1, y = 2;
    swap(&x, &y);
    printf("After swap: x=%d y=%d\n", x, y);
    return 0;
}
