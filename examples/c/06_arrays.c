#include <stdio.h>

int main(void) {
    int numbers[5] = {1, 2, 3, 4, 5};
    size_t count = sizeof numbers / sizeof numbers[0];  /* length, computed */
    int sum = 0;

    for (size_t i = 0; i < count; i++) {
        printf("numbers[%zu] = %d\n", i, numbers[i]);
        sum += numbers[i];
    }
    printf("%zu elements, sum %d\n", count, sum);
    /* C does not check bounds: numbers[5] would read past the end. */
    return 0;
}
