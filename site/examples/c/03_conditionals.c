#include <stdio.h>

static const char *sign(int n) {
    if (n > 0)      return "positive";
    else if (n < 0) return "negative";
    else            return "zero";
}

int main(void) {
    int samples[] = {10, -3, 0};
    for (int i = 0; i < 3; i++)
        printf("%d is %s.\n", samples[i], sign(samples[i]));
    return 0;
}
