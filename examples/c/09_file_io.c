#include <stdio.h>

/* Writes a file, then reads it back one character at a time. */
int main(void) {
    FILE *out = fopen("example.txt", "w");
    if (out == NULL) { perror("fopen"); return 1; }
    fputs("Hello from a file.\n", out);
    fclose(out);

    FILE *in = fopen("example.txt", "r");
    if (in == NULL) { perror("fopen"); return 1; }

    int ch;  /* int, not char: fgetc returns every byte value AND EOF */
    while ((ch = fgetc(in)) != EOF)
        putchar(ch);

    fclose(in);
    return 0;
}
