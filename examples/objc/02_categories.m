#include "Root.h"
#include <stdio.h>

@interface Greeter : Root
- (void)hello;
@end

@implementation Greeter
- (void)hello { printf("hello\n"); }
@end

/* A category adds methods to a class you did not write. */
@interface Greeter (Loud)
- (void)shout;
@end

@implementation Greeter (Loud)
- (void)shout { printf("HELLO\n"); }
@end

int main(void) {
    Greeter *g = [Greeter new];
    [g hello];
    [g shout];
    printf("responds to shout: %s\n",
           [g respondsTo:@selector(shout)] ? "yes" : "no");
    printf("responds to fly: %s\n",
           [g respondsTo:@selector(fly)] ? "yes" : "no");
    [g free];
    return 0;
}
