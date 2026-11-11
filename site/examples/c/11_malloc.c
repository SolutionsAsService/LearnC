#include <stdio.h>
#include <stdlib.h>

int main(void) {
    size_t n = 10;
    int *squares = malloc(n * sizeof *squares);  /* ask the heap */
    if (squares == NULL) return 1;

    for (size_t i = 0; i < n; i++) squares[i] = (int)(i * i);
    printf("squares[9] = %d\n", squares[9]);

    free(squares);    /* you asked, you give it back */
    squares = NULL;   /* and never touch it again */
    return 0;
}
