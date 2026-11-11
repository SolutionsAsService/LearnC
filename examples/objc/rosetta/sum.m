#include "Root.h"
#include <stdio.h>

@interface Counter : Root
+ (int)sumTo:(int)n;
@end

@implementation Counter
+ (int)sumTo:(int)n {
    int s = 0;
    for (int i = 1; i <= n; i++) s += i;
    return s;
}
@end

int main(void) {
    printf("%d\n", [Counter sumTo:10]);
    return 0;
}
