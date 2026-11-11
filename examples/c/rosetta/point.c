#include <math.h>
#include <stdio.h>

struct Point { double x, y; };

double length(struct Point p) { return sqrt(p.x * p.x + p.y * p.y); }

int main(void) {
    struct Point p = {3, 4};
    printf("%.1f\n", length(p));
    return 0;
}
