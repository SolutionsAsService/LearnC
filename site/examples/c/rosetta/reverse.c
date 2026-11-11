#include <stdio.h>
#include <string.h>

int main(void) {
    char s[] = "pointer";
    for (size_t i = 0, j = strlen(s) - 1; i < j; i++, j--) {
        char t = s[i]; s[i] = s[j]; s[j] = t;
    }
    printf("%s\n", s);
    return 0;
}
