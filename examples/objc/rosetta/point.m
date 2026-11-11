#include <math.h>
#include "../Root.h"
#include <stdio.h>

@interface Point : Root {
    double x, y;
}
- (id)initWithX:(double)ax y:(double)ay;
- (double)length;
@end

@implementation Point
- (id)initWithX:(double)ax y:(double)ay { x = ax; y = ay; return self; }
- (double)length { return sqrt(x * x + y * y); }
@end

int main(void) {
    Point *p = [[Point alloc] initWithX:3 y:4];
    printf("%.1f\n", [p length]);
    [p free];
    return 0;
}
