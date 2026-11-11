#include "../Root.h"
#include <stdio.h>
#include <string.h>

@interface Reverser : Root
+ (void)reverse:(char *)s;
@end

@implementation Reverser
+ (void)reverse:(char *)s {
    for (size_t i = 0, j = strlen(s) - 1; i < j; i++, j--) {
        char t = s[i]; s[i] = s[j]; s[j] = t;
    }
}
@end

int main(void) {
    char s[] = "pointer";
    [Reverser reverse:s];
    printf("%s\n", s);
    return 0;
}
