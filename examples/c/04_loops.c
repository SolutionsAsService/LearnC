#include <stdio.h>

int main(void) {
    for (int i = 0; i < 5; i++)          /* counted loop */
        printf("Iteration number: %d\n", i);

    int n = 27, steps = 0;               /* while: run until a condition fails */
    while (n != 1) {
        n = (n % 2 == 0) ? n / 2 : 3 * n + 1;
        steps++;
    }
    printf("27 reaches 1 in %d Collatz steps\n", steps);
    return 0;
}
