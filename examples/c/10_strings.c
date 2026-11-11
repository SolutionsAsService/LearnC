#include <stdio.h>
#include <string.h>

int main(void) {
    char word[] = "pointer";            /* 7 letters + the '\0' terminator */
    size_t n = strlen(word);
    for (size_t i = 0; i < n / 2; i++) { /* reverse in place */
        char t = word[i];
        word[i] = word[n - 1 - i];
        word[n - 1 - i] = t;
    }
    printf("%s (%zu chars, %zu bytes)\n", word, n, sizeof word);
    return 0;
}
